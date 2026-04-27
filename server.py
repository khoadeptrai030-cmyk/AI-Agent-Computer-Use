"""
🌐 WEB SERVER - Dashboard GUI cho AI Agent
=============================================
Chạy Flask + SocketIO server để:
1. Hiển thị dashboard web (giống Antigravity)
2. Truyền ảnh live screen feed
3. Hiển thị thought/action logs real-time
4. Điều khiển start/stop task

Cách chạy: python server.py
Mở trình duyệt: http://localhost:5000
"""

import os
import sys
import time
import threading
import base64
from io import BytesIO
from datetime import datetime

# Fix encoding
if sys.platform == "win32":
    os.system("")
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from flask import Flask, render_template
from flask_socketio import SocketIO

import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ai-agent-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Global state
agent_thread = None
stop_event = threading.Event()


# ═══════════════════════════════════════════════════════════════
# ROUTES
# ═══════════════════════════════════════════════════════════════

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    return {'status': 'running' if agent_thread and agent_thread.is_alive() else 'ready'}


# ═══════════════════════════════════════════════════════════════
# SOCKET EVENTS
# ═══════════════════════════════════════════════════════════════

import subprocess

@socketio.on('start_task')
def handle_start_task(data):
    global agent_thread, stop_event

    task = data.get('task', '').strip()
    if not task:
        socketio.emit('error', {'text': 'Vui lòng nhập nhiệm vụ!'})
        return

    if agent_thread and agent_thread.is_alive():
        socketio.emit('error', {'text': 'Agent đang chạy! Hãy dừng trước.'})
        return

    stop_event.clear()
    
    # Khởi động overlay nếu được bật
    if getattr(config, 'SHOW_OVERLAY', True):
        try:
            if os.path.exists(".venv/Scripts/python.exe"):
                python_exec = ".venv/Scripts/python.exe"
            else:
                python_exec = "python"
            global overlay_proc
            overlay_proc = subprocess.Popen([python_exec, "overlay.py"])
        except Exception as e:
            print("Lỗi mở overlay:", e)

    agent_thread = threading.Thread(target=run_agent_task, args=(task,), daemon=True)
    agent_thread.start()


def cleanup_overlay():
    try:
        global overlay_proc
        if 'overlay_proc' in globals() and overlay_proc:
            overlay_proc.terminate()
            overlay_proc = None
    except Exception:
        pass

@socketio.on('stop_task')
def handle_stop_task():
    global stop_event
    stop_event.set()
    socketio.emit('stopped', {'text': 'Agent đã được yêu cầu dừng.'})
    cleanup_overlay()

@app.route('/api/stop', methods=['POST', 'GET'])
def api_stop():
    handle_stop_task()
    return {"status": "stopped"}


# ═══════════════════════════════════════════════════════════════
# AGENT LOOP (runs in background thread)
# ═══════════════════════════════════════════════════════════════

def run_agent_task(task: str):
    """Chạy Agent trong background thread, gửi events qua SocketIO."""
    try:
        # Lazy imports to avoid circular deps
        from vision import vision
        from brain import brain
        from actions import actions
        
        brain.reset()
        
        step = 0
        consecutive_errors = 0
        max_consecutive_errors = 5
        
        socketio.emit('step', {'step': 0, 'max_steps': config.MAX_STEPS})
    except Exception as e:
        socketio.emit('error', {'text': f'Lỗi khởi tạo Agent: {str(e)}'})
        socketio.emit('done', {'text': 'Agent bị crash lúc khởi động.'})
        cleanup_overlay()
        return
    
    while step < config.MAX_STEPS and not stop_event.is_set():
        step += 1
        socketio.emit('step', {'step': step, 'max_steps': config.MAX_STEPS})
        
        try:
            # ─── 1. OBSERVE ─────────────────────────────────
            screenshot = vision.get_screenshot_for_ai()
            
            # Gửi ảnh live lên dashboard
            try:
                buf = BytesIO()
                screenshot.save(buf, format='JPEG', quality=60)
                img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                socketio.emit('screenshot', {'image': img_b64})
            except Exception:
                pass
            
            # ─── 2. ORIENT ──────────────────────────────────
            system_context = vision.get_system_context()
            
            # ─── 3. DECIDE ──────────────────────────────────
            action_data = brain.think(
                task=task,
                screenshot=screenshot,
                system_context=system_context
            )
            
            # Emit provider info
            if brain.working_provider:
                socketio.emit('provider', {'name': brain.working_provider.__name__})
            
            if action_data is None:
                consecutive_errors += 1
                socketio.emit('error', {
                    'text': f'AI không phản hồi ({consecutive_errors}/{max_consecutive_errors})'
                })
                if consecutive_errors >= max_consecutive_errors:
                    socketio.emit('done', {'text': 'Quá nhiều lỗi liên tiếp. Dừng Agent.'})
                    cleanup_overlay()
                    return
                time.sleep(2)
                continue
            
            consecutive_errors = 0
            
            # Emit thought
            thought = action_data.get('thought', 'Không có suy nghĩ')
            socketio.emit('thought', {'text': thought})
            
            # ─── 4. ACT ─────────────────────────────────────
            action_type = action_data.get('action_type', 'unknown')
            details_dict = {k: v for k, v in action_data.items() if k not in ['thought']}
            
            is_done, message = actions.execute(action_data)
            
            socketio.emit('action', {
                'type': action_type,
                'details': message,
                'count': actions.action_count
            })
            
            if is_done:
                socketio.emit('done', {'text': message})
                cleanup_overlay()
                return
            
            # ─── 5. WAIT ────────────────────────────────────
            time.sleep(config.STEP_DELAY)
            
        except Exception as e:
            consecutive_errors += 1
            socketio.emit('error', {'text': f'Lỗi hệ thống: {str(e)}'})
            
            if consecutive_errors >= max_consecutive_errors:
                socketio.emit('done', {'text': 'Quá nhiều lỗi. Dừng Agent.'})
                cleanup_overlay()
                break
            time.sleep(2)
    
    if stop_event.is_set():
        socketio.emit('stopped', {'text': 'Agent đã dừng theo yêu cầu.'})
    else:
        socketio.emit('done', {'text': f'Đã hết {config.MAX_STEPS} bước. Nhiệm vụ có thể chưa hoàn thành.'})

    # Dọn dẹp overlay khi task kết thúc
    cleanup_overlay()


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("  🤖 AI Agent Computer Use — Dashboard")
    print("=" * 60)
    print(f"  🌐 Mở trình duyệt: http://localhost:5000")
    print(f"  🛑 Dừng server: Ctrl+C")
    print("=" * 60 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
