# ❓ FAQ & Xử Lý Sự Cố (Troubleshooting)

Giải pháp cho các vấn đề thường gặp.

---

## 📋 Mục Lục

### Installation Issues
- [Python không cài đặt](#python-không-cài-đặt)
- [Virtual environment lỗi](#virtual-environment-lỗi)
- [Dependencies cài đặt thất bại](#dependencies-cài-đặt-thất-bại)

### Runtime Issues
- [Agent không hoạt động](#agent-không-hoạt động)
- [G4F providers không kết nối](#g4f-providers-không-kết-nối)
- [Screenshot/Vision không hoạt động](#screenshotvision-không-hoạt-động)

### Automation Issues
- [Agent click nhầm](#agent-click-nhầm)
- [Gõ chữ bị lỗi](#gõ-chữ-bị-lỗi)
- [Agent stuck / loop vô hạn](#agent-stuck--loop-vô-hạn)

### Dashboard Issues
- [Web dashboard không hiển thị](#web-dashboard-không-hiển-thị)
- [Cập nhật real-time lag](#cập-nhật-real-time-lag)

### Performance Issues
- [Máy chạy chậm / lag](#máy-chạy-chậm--lag)
- [Memory leak](#memory-leak)

### Platform-specific Issues
- [macOS accessibility permissions](#macos-accessibility-permissions)
- [Linux input device permissions](#linux-input-device-permissions)
- [Windows Terminal encoding](#windows-terminal-encoding)

---

## 💻 Installation Issues

### Python Không Cài Đặt

**Triệu chứng:**
```
'python' is not recognized as an internal or external command
```

**Fix:**

1. **Download Python** từ [python.org](https://www.python.org/downloads/)
2. **Cài đặt** - ⭐ **QUAN TRỌNG**: Tick "Add Python to PATH"
3. **Restart** terminal
4. **Kiểm tra**:
   ```bash
   python --version
   python -m pip --version
   ```

**Nếu vẫn lỗi:**
```bash
# Windows - Dùng full path
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe --version

# Hoặc dùng py launcher
py --version
py -m pip install g4f
```

---

### Virtual Environment Lỗi

**Triệu chứng:**
```
Error: No module named 'venv'
```

**Fix:**

```bash
# Windows - Install venv
python -m pip install --upgrade pip setuptools wheel

# Linux/macOS
python3 -m venv .venv

# Nếu vẫn lỗi - install manually
pip install virtualenv
virtualenv .venv

# Activate
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

**Venv không kích hoạt?**

```bash
# ❌ Sai
python main.py

# ✓ Đúng
.venv\Scripts\activate  # Kích hoạt trước!
python main.py

# Kiểm tra (nếu OK, sẽ có (.venv) ở prompt)
(.venv) D:\Use Computer> _
```

---

### Dependencies Cài Đặt Thất Bại

**Triệu chứng:**
```
ERROR: Failed building wheel for opencv-python
ERROR: Could not find a version that satisfies the requirement
```

**Fix:**

**Cách 1: Cài từng package, kiểm tra error**
```bash
pip install g4f
pip install pyautogui
pip install pynput
# ... etc
```

**Cách 2: Upgrade pip trước**
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Cách 3: Use pre-built wheels**
```bash
# Tải từ https://www.lfd.uci.edu/~gohlke/pythonlibs/
# Ví dụ: opencv_python‑4.8.0‑cp311‑cp311‑win_amd64.whl
pip install opencv_python‑4.8.0‑cp311‑cp311‑win_amd64.whl
```

**Cách 4: Use headless version**
```bash
pip install opencv-python-headless  # Thay vì opencv-python
```

**Cách 5: Install C++ build tools (Windows)**
```bash
# Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Hoặc: winget install Microsoft.VisualStudio.VC++.BuildTools
```

---

## 🚀 Runtime Issues

### Agent Không Hoạt Động

**Triệu chứng:**
```
agent doesn't respond, stuck, or exits immediately
```

**Fix:**

**Bước 1: Kiểm tra imports**
```bash
python -c "import g4f; print('G4F OK')"
python -c "import pyautogui; print('PyAutoGUI OK')"
python -c "from brain import Brain; print('Brain OK')"
```

**Bước 2: Kiểm tra config**
```bash
python -c "import config; print(f'Width: {config.SCREEN_WIDTH}, Height: {config.SCREEN_HEIGHT}')"
```

**Bước 3: Run dengan debug**
```bash
LOG_LEVEL=DEBUG python main.py
```

**Bước 4: Check errors**
```bash
# Xem full traceback
python -u main.py 2>&1 | tee debug.log
```

---

### G4F Providers Không Kết Nối

**Triệu chứng:**
```
Error: Failed to connect to all available providers
Error: Rate limit exceeded
Connection timeout
```

**Fix:**

**Bước 1: Kiểm tra internet**
```bash
ping 8.8.8.8

# Hoặc test direct
curl https://api.example.com
```

**Bước 2: Cập nhật G4F**
```bash
pip install --upgrade g4f
```

**Bước 3: Kiểm tra providers**
```python
from g4f.client import Client
from g4f.Provider import RetryProvider

client = Client()

# List available providers
print(client.get_available_providers())

# Test một provider
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}],
    timeout=30
)
print(response.choices[0].message.content)
```

**Bước 4: Tăng delay để tránh rate limit**
```python
# config.py
STEP_DELAY = 20.0  # Từ 12s lên 20s
MAX_RETRIES = 5    # Thử lại nhiều lần hơn
```

**Bước 5: Proxy (nếu cần)**
```python
# brain.py
import g4f
proxy = "http://proxy.company.com:8080"

client = g4f.Client(
    proxy=proxy,
    timeout=30
)
```

---

### Screenshot/Vision Không Hoạt Động

**Triệu chứng:**
```
No image captured
Screenshot is black/blank
Error: Cannot grab monitor
```

**Fix:**

**Windows:**
```python
# config.py - Điều chỉnh độ phân giải
SCREEN_WIDTH = 1920   # Check System Settings
SCREEN_HEIGHT = 1080

# Hoặc auto-detect
import pyautogui
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
```

**macOS:**
```bash
# Cấp quyền screen recording
System Preferences > Security & Privacy > Screen Recording > Terminal

# Hoặc
sudo nano /etc/sudoers.d/cvprivs
# Thêm:
# %admin ALL = (ALL) /System/Library/CoreServices/ScreenLockUIAgent
```

**Linux:**
```bash
# Kiểm tra DISPLAY
echo $DISPLAY  # Nên là :0 hoặc :1

# Nếu không set
export DISPLAY=:0
python main.py
```

**Check MSS (screenshot library):**
```python
import mss
with mss.mss() as sct:
    monitors = sct.monitors
    print(f"Found {len(monitors)} monitors")
    for i, m in enumerate(monitors):
        print(f"Monitor {i}: {m}")
```

---

## 🎮 Automation Issues

### Agent Click Nhầm

**Triệu chứng:**
```
Chuột click vào vị trí sai (cách xa target)
Agent không thể tìm buttons/inputs
```

**Fix:**

**Bước 1: Check độ phân giải**
```python
# config.py
import pyautogui
print(f"Actual screen size: {pyautogui.size()}")

# Phải khớp với:
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
```

**Bước 2: Bật SHOW_OVERLAY để visualize**
```python
# config.py
SHOW_OVERLAY = True  # Hiển thị grid overlay

# Chạy
python main.py

# Xem grid có khớp không
```

**Bước 3: Tăng grid resolution**
```python
# config.py - Default là 16x10
GRID_ROWS = 12     # Từ 10 lên 12 (chi tiết hơn)
GRID_COLS = 20     # Từ 16 lên 20
```

**Bước 4: Test vision module**
```bash
python test_vision.py

# Xem screenshot có được capture đúng không
# Xem trong folder screenshots/
```

**Bước 5: Manual test**
```python
from actions import Actions
import time

actions = Actions()

# Test click vào góc màn hình
actions.left_click(50, 50)
time.sleep(1)

# Kiểm tra chuột có đó không (visual)
input("Did mouse click in top-left? (y/n): ")
```

---

### Gõ Chữ Bị Lỗi

**Triệu chứng:**
```
Gõ "Xin chào" → hiện "Xin ch o" hoặc gibberish
Unicode characters bị messed up
```

**Fix:**

**Windows:**
```python
# actions.py hoặc main.py - thêm vào đầu
import sys
sys.stdout.reconfigure(encoding='utf-8')

# config.py
import os
os.system("")  # Enable ANSI

# Hoặc test
from actions import Actions
a = Actions()
a.type_text("Xin chào Việt Nam")  # Nên hoạt động
```

**macOS/Linux:**
```bash
# Check locale
locale

# Set UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Test
python -c "print('Xin chào')"
```

**Nếu vẫn lỗi - Dùng clipboard:**
```python
import pyperclip
from actions import Actions

text = "Xin chào Việt Nam"
pyperclip.copy(text)  # Copy vào clipboard

actions = Actions()
actions.hotkey("ctrl", "v")  # Paste
```

---

### Agent Stuck / Loop Vô Hạn

**Triệu chứng:**
```
Agent thực hiện cùng một hành động liên tục
Không tiến bộ, không kết thúc
```

**Fix:**

**Bước 1: Dừng ngay**
```bash
# Nhấn Ctrl+C
Ctrl+C

# Hoặc di chuột vào góc trên bên trái (Emergency Stop)

# Hoặc kill process
kill -9 $(pgrep -f "python main.py")  # Linux/macOS
taskkill /IM python.exe /F             # Windows
```

**Bước 2: Kiểm tra logs**
```bash
python main.py 2>&1 | tee debug.log
# Xem file debug.log để tìm pattern lặp
```

**Bước 3: Giảm MAX_STEPS**
```python
# config.py
MAX_STEPS = 15  # Từ 30 xuống 15 (dừng sớm hơn)
```

**Bước 4: Tăng step delay**
```python
# config.py
STEP_DELAY = 15.0  # Từ 12s lên 15s (wait lâu hơn)
```

**Bước 5: Improve system prompt**
```python
# brain.py
SYSTEM_PROMPT = """
...
IMPORTANT: If you're repeating the same action, STOP and say "CANNOT_PROCEED"
...
"""
```

---

## 🌐 Dashboard Issues

### Web Dashboard Không Hiển Thị

**Triệu chứng:**
```
Open http://localhost:5000 → blank page / 404 / connection refused
```

**Fix:**

**Bước 1: Kiểm tra server chạy**
```bash
# Terminal 1 - Chạy agent
python main.py

# Terminal 2 - Chạy server
python server.py

# Output nên có:
# * Running on http://0.0.0.0:5000
```

**Bước 2: Kiểm tra port**
```bash
# Check port 5000 được dùng
netstat -an | grep 5000           # macOS/Linux
netstat -ano | findstr 5000       # Windows

# Nếu occupied, đổi port
# Trong server.py
app.run(port=8000, debug=False)

# Hoặc kill process
kill -9 $(lsof -ti:5000)  # macOS/Linux
```

**Bước 3: Check Flask cài đặt**
```bash
pip install --upgrade flask flask-socketio python-socketio
```

**Bước 4: Check firewall**
```bash
# Có thể port bị block
# Windows Defender Firewall:
# → Allow app through firewall → Python

# Linux iptables
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
```

**Bước 5: Debug server**
```bash
DEBUG=1 python server.py
# hoặc trong server.py
app.run(port=5000, debug=True)  # Debug mode
```

---

### Cập Nhật Real-time Lag

**Triệu chứng:**
```
Dashboard updates slow
Screenshot feed choppy
Logs delayed
```

**Fix:**

**Bước 1: Reduce screenshot quality**
```python
# config.py
SCREENSHOT_QUALITY = 50  # Từ 90 xuống 50 (nhỏ hơn)

# hoặc trong server.py
SCREENSHOT_QUALITY = 70
```

**Bước 2: Disable grid**
```python
# config.py
GRID_ENABLED = False  # Tắt grid để tiết kiệm tài nguyên
```

**Bước 3: Increase step delay**
```python
# config.py
STEP_DELAY = 15.0  # Chậm xuống để server kịp xử lý
```

**Bước 4: Limit logs**
```python
# server.py
MAX_LOGS = 500  # Từ 1000 xuống 500 (ít logs hơn)
```

**Bước 5: Run on better hardware**
```bash
# Hoặc dùng Docker với resource limit
docker run --cpus=4 --memory=4g ai-agent
```

---

## 💾 Performance Issues

### Máy Chạy Chậm / Lag

**Triệu chứng:**
```
CPU 100%, RAM full
Máy không phản ứng
Other apps lag
```

**Fix:**

**Bước 1: Giảm frequency**
```python
# config.py
STEP_DELAY = 20.0  # Tăng delay (ít request hơn)
```

**Bước 2: Disable unnecessary features**
```python
# config.py
GRID_ENABLED = False       # Tắt grid
SHOW_OVERLAY = False       # Tắt overlay
SAVE_SCREENSHOTS = False   # Không save screenshots
```

**Bước 3: Reduce resolution**
```python
# Capture ảnh nhỏ hơn
# Chỉnh trong vision.py

# Hoặc scale down before sending to AI
img = img.resize((img.width // 2, img.height // 2))
```

**Bước 4: Use headless mode**
```bash
# Chạy server mà không có GUI
python server.py --headless
```

**Bước 5: Monitor resources**
```bash
# Watch CPU/Memory
watch -n 1 'ps aux | grep python'  # Linux
# hoặc
Activity Monitor  # macOS
Task Manager      # Windows
```

---

### Memory Leak

**Triệu chứng:**
```
Memory usage increases over time
Agent runs fine for 1 hour, then slows down after 8 hours
```

**Fix:**

**Bước 1: Check memory usage**
```python
import psutil
import os

process = psutil.Process(os.getpid())
print(f"Memory: {process.memory_info().rss / 1024 / 1024:.2f} MB")
```

**Bước 2: Investigate logs/screenshots**
```bash
# Clear old screenshots periodically
rm screenshots/step_*.png

# Hoặc trong code
import os
import glob
for f in glob.glob("screenshots/*"):
    if os.path.getmtime(f) < time.time() - 3600:  # Older than 1 hour
        os.remove(f)
```

**Bước 3: Clear cache**
```python
# brain.py - Clear history periodically
if len(self.history) > 100:
    self.history = self.history[-50:]  # Keep only last 50
```

**Bước 4: Restart periodically**
```bash
# Script to restart every 24 hours
while true; do
    python main.py
    sleep 86400  # 24 hours
done
```

---

## 🖥️ Platform-specific Issues

### macOS Accessibility Permissions

**Triệu chứng:**
```
PyAutoGUI not working (mouse/keyboard)
Airplane on screen but can't move
```

**Fix:**

**Cách 1: System Preferences**
1. System Preferences → Security & Privacy
2. Select "Privacy" tab (left side)
3. Click "Accessibility" 
4. Click **+** button
5. Select **Terminal** (hoặc IDE của bạn)
6. Grant access
7. Restart Terminal

**Cách 2: Command line**
```bash
# Open file in nano
sudo nano /Library/Application\ Support/CrashReporter/.symlinks

# Grant Terminal access
sudo sqlite3 /Library/Application\ Support/com.apple.sharedfilelist add-domain '/Library/Application\ Support/CrashReporter/.symlinks' 'com.apple.trust-settings' 'admin' '/usr/local/bin/python3' 1

# Restart Terminal
```

**Cách 3: Check permission**
```python
import pyautogui
try:
    pyautogui.moveTo(100, 100)
    print("✓ Accessibility OK")
except Exception as e:
    print(f"✗ Accessibility denied: {e}")
```

---

### Linux Input Device Permissions

**Triệu chứng:**
```
Permission denied accessing /dev/input
Can't control mouse/keyboard
```

**Fix:**

```bash
# Add user to input group
sudo usermod -a -G input $USER

# Apply changes (logout/login or)
newgrp input

# Verify
groups  # Should include "input"

# Test
python main.py
```

**Nếu vẫn lỗi:**
```bash
# Run with sudo (not recommended)
sudo python main.py

# Hoặc setup udev rules
sudo nano /etc/udev/rules.d/50-mouse-keyboard.rules

# Add:
# SUBSYSTEM=="input", MODE="0666"
# SUBSYSTEM=="usb", MODE="0666"

# Reload rules
sudo udevadm control --reload-rules
sudo udevadm trigger
```

---

### Windows Terminal Encoding

**Triệu chứng:**
```
Terminal output shows ??? instead of Vietnamese
Chữ tiếng Việt không hiển thị đúng
```

**Fix:**

**Cách 1: Python auto-fix (trong code)**
```python
import sys
import os

if sys.platform == "win32":
    os.system("")  # Enable ANSI escape codes
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
```

**Cách 2: Set system locale**
```bash
# PowerShell (Admin)
Set-Culture vi-VN

# Hoặc command prompt
chcp 65001  # UTF-8
```

**Cách 3: Use Windows Terminal (recommended)**
```bash
# Download: https://aka.ms/terminal
# Có native UTF-8 support
```

---

## 📞 Tìm Kiếm Trợ Giúp

Nếu vấn đề không liệt kê ở trên:

1. **Check logs**
   ```bash
   tail -f agent.log  # Latest logs
   ```

2. **Search issues**
   - [GitHub Issues](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues)

3. **Ask community**
   - [Discussions](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/discussions/1)

4. **Create issue**
   ```markdown
   ## Issue: [Title]
   
   ### Environment
   - OS: Windows 10
   - Python: 3.10
   - OS: [browser version]
   
   ### Description
   Mô tả vấn đề
   
   ### Steps to Reproduce
   1. ...
   2. ...
   
   ### Expected vs Actual
   Cái gì diễn ra vs cái gì nên diễn ra
   
   ### Logs
   ```
   Paste error/logs ở đây
   ```
   
   ### Already Tried
   - Cái gì bạn đã thử fix?
   ```

---

## ✅ Final Checklist

Trước khi báo cáo issue:

- [ ] Đã googled error message
- [ ] Đã kiểm tra [Issues](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues) cũ
- [ ] Đã cập nhật package (`pip install --upgrade`)
- [ ] Đã restart terminal/máy
- [ ] Đã try solution trong troubleshooting này
- [ ] Có thể reproduce vấn đề consistently

---

**Still stuck? Mở [Discussion](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/discussions/1) hoặc [Issue](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues) nhé! 🆘**

**Happy debugging! 🔧**
