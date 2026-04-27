"""
🤖 AI AGENT COMPUTER USE - Main Controller
=============================================
Đây là file chính - vòng lặp OODA:
  Observe (Quan sát) → Orient (Định hướng) → Decide (Quyết định) → Act (Hành động)

Cách chạy:
  python main.py

Agent sẽ:
1. Hỏi bạn muốn làm gì
2. Chụp ảnh màn hình 
3. Gửi ảnh cho AI phân tích
4. Thực hiện hành động
5. Lặp lại cho đến khi hoàn thành hoặc hết bước

DỪNG KHẨN CẤP: Di chuột vào góc trên bên trái màn hình!
"""

import os
import sys
import time
import signal
from datetime import datetime

# Fix encoding cho Windows terminal
if sys.platform == "win32":
    os.system("")  # Enable ANSI escape codes on Windows
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from colorama import init, Fore, Style, Back
init(autoreset=True)

import config


# ═══════════════════════════════════════════════════════════════
# BANNER & UI
# ═══════════════════════════════════════════════════════════════

BANNER = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {Fore.WHITE}█████╗ ██╗     █████╗  ██████╗ ███████╗███╗   ██╗████████╗{Fore.CYAN}  ║
║  {Fore.WHITE}██╔══██╗██║    ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝{Fore.CYAN}  ║
║  {Fore.WHITE}███████║██║    ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║{Fore.CYAN}     ║
║  {Fore.WHITE}██╔══██║██║    ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║{Fore.CYAN}     ║
║  {Fore.WHITE}██║  ██║██████╗██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║{Fore.CYAN}     ║
║  {Fore.WHITE}╚═╝  ╚═╝╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝{Fore.CYAN}     ║
║                                                              ║
║  {Fore.YELLOW}🤖 AI Computer Use Agent - Free & Unlimited{Fore.CYAN}                ║
║  {Fore.GREEN}⚡ Powered by G4F | No API Key Required{Fore.CYAN}                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""

def print_status(label: str, value: str, color=Fore.WHITE):
    """In trạng thái với format đẹp."""
    print(f"  {Fore.CYAN}│ {Fore.WHITE}{label}: {color}{value}{Style.RESET_ALL}")

def print_step_header(step: int, max_steps: int):
    """In header cho mỗi bước."""
    print(f"\n{Fore.YELLOW}{'━' * 60}")
    print(f"  📍 BƯỚC {step}/{max_steps}")
    print(f"{'━' * 60}{Style.RESET_ALL}")

def print_thought(thought: str):
    """In suy nghĩ của AI."""
    print(f"\n  {Fore.MAGENTA}💭 Suy nghĩ: {Fore.WHITE}{thought}{Style.RESET_ALL}")

def print_action(action_type: str, details: str):
    """In hành động được thực hiện."""
    print(f"  {Fore.GREEN}🖐️ Hành động: {Fore.WHITE}{action_type} → {details}{Style.RESET_ALL}")

def print_error(msg: str):
    """In lỗi."""
    print(f"  {Fore.RED}❌ {msg}{Style.RESET_ALL}")

def print_warning(msg: str):
    """In cảnh báo."""
    print(f"  {Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def print_success(msg: str):
    """In thành công."""
    print(f"  {Fore.GREEN}✅ {msg}{Style.RESET_ALL}")


# ═══════════════════════════════════════════════════════════════
# VÒNG LẶP CHÍNH (OODA LOOP)
# ═══════════════════════════════════════════════════════════════

def run_agent(task: str):
    """
    Vòng lặp tự chủ chính của AI Agent.
    
    OODA Loop:
      1. OBSERVE: Chụp ảnh màn hình
      2. ORIENT: Thu thập thông tin hệ thống
      3. DECIDE: Gửi cho AI, nhận quyết định
      4. ACT: Thực hiện hành động
      5. Lặp lại
    """
    # Import ở đây để tránh circular import và hiện lỗi rõ ràng
    from vision import vision
    from brain import brain
    from actions import actions
    
    print(f"\n{Fore.CYAN}{'═' * 60}")
    print(f"  🎯 NHIỆM VỤ: {Fore.WHITE}{task}")
    print(f"{Fore.CYAN}{'═' * 60}{Style.RESET_ALL}\n")
    
    # Reset brain cho nhiệm vụ mới
    brain.reset()
    
    step = 0
    consecutive_errors = 0
    max_consecutive_errors = 3
    
    while step < config.MAX_STEPS:
        step += 1
        print_step_header(step, config.MAX_STEPS)
        
        try:
            # ─── 1. OBSERVE: Chụp ảnh ─────────────────────────
            print(f"  {Fore.CYAN}👁️  Đang quan sát màn hình...{Style.RESET_ALL}")
            screenshot = vision.get_screenshot_for_ai()
            
            # ─── 2. ORIENT: Thu thập context ────────────────────
            system_context = vision.get_system_context()
            
            # ─── 3. DECIDE: Hỏi AI ────────────────────────────
            print(f"  {Fore.CYAN}🧠 Đang suy nghĩ...{Style.RESET_ALL}")
            
            action_data = brain.think(
                task=task,
                screenshot=screenshot,
                system_context=system_context
            )
            
            if action_data is None:
                consecutive_errors += 1
                print_error(f"AI không phản hồi (lỗi liên tiếp: {consecutive_errors}/{max_consecutive_errors})")
                
                if consecutive_errors >= max_consecutive_errors:
                    print_error("Quá nhiều lỗi liên tiếp. Dừng Agent.")
                    break
                
                time.sleep(2)
                continue
            
            # Reset error counter khi thành công
            consecutive_errors = 0
            
            # In suy nghĩ
            thought = action_data.get("thought", "Không có suy nghĩ")
            print_thought(thought)
            
            # ─── 4. ACT: Thực hiện ────────────────────────────
            action_type = action_data.get("action_type", "unknown")
            print_action(action_type, str({k: v for k, v in action_data.items() if k not in ["thought"]}))
            
            is_done, message = actions.execute(action_data)
            
            if is_done:
                print(f"\n{Fore.GREEN}{'═' * 60}")
                print(f"  🎉 {message}")
                print(f"  📊 Tổng số bước: {step}")
                print(f"  📊 Tổng hành động: {actions.action_count}")
                print(f"{'═' * 60}{Style.RESET_ALL}\n")
                return True
            
            print(f"  {Fore.WHITE}→ {message}{Style.RESET_ALL}")
            
            # ─── 5. CHỜ UI PHẢN HỒI ───────────────────────────
            print(f"  {Fore.CYAN}⏳ Chờ {config.STEP_DELAY}s...{Style.RESET_ALL}")
            time.sleep(config.STEP_DELAY)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}⏹️  Người dùng dừng Agent (Ctrl+C){Style.RESET_ALL}")
            return False
        except Exception as e:
            consecutive_errors += 1
            print_error(f"Lỗi hệ thống: {str(e)}")
            
            if consecutive_errors >= max_consecutive_errors:
                print_error("Quá nhiều lỗi. Dừng Agent.")
                break
            
            time.sleep(2)
    
    print(f"\n{Fore.YELLOW}{'═' * 60}")
    print(f"  ⏰ Đã đạt giới hạn {config.MAX_STEPS} bước.")
    print(f"  Nhiệm vụ có thể chưa hoàn thành.")
    print(f"{'═' * 60}{Style.RESET_ALL}\n")
    return False


# ═══════════════════════════════════════════════════════════════
# INTERACTIVE MODE
# ═══════════════════════════════════════════════════════════════

def interactive_mode():
    """
    Chế độ tương tác: nhập nhiệm vụ liên tục.
    Gõ 'quit' hoặc 'exit' để thoát.
    """
    print(BANNER)
    
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print_status("Trạng thái", "ONLINE", Fore.GREEN)
    print_status("Chế độ", "INTERACTIVE", Fore.YELLOW)
    print_status("Màn hình", f"{config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}", Fore.WHITE)
    print_status("Grid", f"{config.GRID_COLS}x{config.GRID_ROWS} ({config.GRID_COLS * config.GRID_ROWS} ô)", Fore.WHITE)
    print_status("Max bước", str(config.MAX_STEPS), Fore.WHITE)
    print_status("Dừng khẩn cấp", "Di chuột vào GÓC TRÊN TRÁI", Fore.RED)
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    # Khởi tạo providers
    print(f"\n{Fore.CYAN}🔌 Đang kiểm tra AI providers...{Style.RESET_ALL}")
    from brain import brain
    
    if brain.providers:
        print(f"{Fore.GREEN}  ✅ {len(brain.providers)} provider(s) sẵn sàng!{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}  ⚠️  Không tìm thấy provider ưu tiên. Sẽ dùng auto-detect.{Style.RESET_ALL}")
    
    print(f"\n{Fore.WHITE}{'─' * 60}")
    print(f"  Nhập nhiệm vụ cho AI Agent.")
    print(f"  Ví dụ: 'Mở Notepad và gõ Hello World'")
    print(f"  Gõ 'quit' để thoát.")
    print(f"{'─' * 60}{Style.RESET_ALL}\n")
    
    while True:
        try:
            task = input(f"{Fore.YELLOW}🎯 Nhiệm vụ > {Fore.WHITE}").strip()
            
            if not task:
                continue
            
            if task.lower() in ("quit", "exit", "q", "thoát"):
                print(f"\n{Fore.CYAN}👋 Tạm biệt! Agent đã tắt.{Style.RESET_ALL}\n")
                break
            
            if task.lower() == "help":
                print(f"""
{Fore.CYAN}📖 HƯỚNG DẪN SỬ DỤNG:{Style.RESET_ALL}
  
  {Fore.WHITE}Bạn có thể ra lệnh bằng tiếng Việt hoặc tiếng Anh:{Style.RESET_ALL}
  
  {Fore.GREEN}• Mở Notepad và gõ 'Xin chào thế giới'{Style.RESET_ALL}
  {Fore.GREEN}• Mở Chrome vào youtube.com{Style.RESET_ALL}
  {Fore.GREEN}• Tìm kiếm 'AI Agent' trên Google{Style.RESET_ALL}
  {Fore.GREEN}• Mở File Explorer và tạo folder mới tên 'test'{Style.RESET_ALL}
  {Fore.GREEN}• Chụp ảnh màn hình và lưu vào Desktop{Style.RESET_ALL}
  
  {Fore.YELLOW}Lệnh đặc biệt:{Style.RESET_ALL}
    quit/exit  - Thoát
    help       - Hiện hướng dẫn này
""")
                continue
            
            # Chạy task
            start_time = time.time()
            success = run_agent(task)
            elapsed = time.time() - start_time
            
            if success:
                print_success(f"Hoàn thành trong {elapsed:.1f} giây!")
            else:
                print_warning(f"Nhiệm vụ kết thúc sau {elapsed:.1f} giây (có thể chưa hoàn thành)")
            
            print()  # Dòng trống
            
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}👋 Tạm biệt!{Style.RESET_ALL}\n")
            break
        except EOFError:
            break


# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Xử lý argument dòng lệnh
    if len(sys.argv) > 1:
        # Chạy trực tiếp với task từ command line
        task = " ".join(sys.argv[1:])
        print(BANNER)
        run_agent(task)
    else:
        # Chế độ tương tác
        interactive_mode()
