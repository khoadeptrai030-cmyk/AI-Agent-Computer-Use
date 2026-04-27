# 🤖 AI Agent — Computer Use with G4F

<div align="center">

![AI Agent Banner](https://img.shields.io/badge/AI%20Agent-Computer%20Control-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge)
![G4F](https://img.shields.io/badge/G4F-Free%20AI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Tạo một AI Agent tự động hóa các tác vụ máy tính của bạn — hoàn toàn miễn phí, không cần API keys!**

[Tính Năng](#-tính-năng) • [Cài Đặt](#-cài-đặt) • [Cách Dùng](#-cách-dùng) • [Ví Dụ](#-ví-dụ) • [Cấu Hình](#-cấu-hình) • [FAQ](#-faq)

</div>

---

## 📋 Mục Lục

1. [Giới Thiệu](#-giới-thiệu)
2. [Tính Năng](#-tính-năng)
3. [Yêu Cầu Hệ Thống](#-yêu-cầu-hệ-thống)
4. [Cài Đặt](#-cài-đặt)
5. [Cách Dùng](#-cách-dùng)
6. [Ví Dụ Thực Tế](#-ví-dụ-thực-tế)
7. [Kiến Trúc](#-kiến-trúc)
8. [Cấu Hình Chi Tiết](#-cấu-hình-chi-tiết)
9. [Web Dashboard](#-web-dashboard)
10. [API Reference](#-api-reference)
11. [Lưu Ý An Toàn](#-lưu-ý-an-toàn)
12. [Xử Lý Sự Cố](#-xử-lý-sự-cố)
13. [Đóng Góp](#-đóng-góp)
14. [License](#-license)

---

## 🎯 Giới Thiệu

**AI Agent — Computer Use** là một dự án mã nguồn mở cho phép bạn tạo một AI agent tự động hóa **bất kỳ tác vụ nào** trên máy tính của bạn:

- ✅ **Không cần API keys** — Sử dụng G4F (GPT4Free) — AI providers miễn phí
- ✅ **Thị giác máy tính** — Chụp ảnh màn hình, phân tích bằng AI
- ✅ **Điều khiển toàn bộ** — Click chuột, gõ bàn phím, mở ứng dụng
- ✅ **Vòng lặp OODA** — Quan sát → Định hướng → Quyết định → Hành động
- ✅ **Dashboard Web** — Giám sát real-time qua trình duyệt
- ✅ **Hoàn toàn offline** — Chạy 100% trên máy của bạn
- ✅ **An toàn** — Có nút dừng khẩn cấp (Emergency Stop)

**Ý tưởng**: Agent bạn một cách thông minh. Hãy cho nó một tác vụ, nó sẽ tự thực hiện như một người thật!

---

## 🚀 Tính Năng

### Core Features

| Tính Năng | Chi Tiết |
|-----------|---------|
| 🧠 **Bộ Não AI** | Sử dụng G4F để kết nối các AI provider miễn phí (Claude, GPT-4 Free, v.v.) |
| 👁️ **Computer Vision** | Chụp ảnh màn hình + Grid System để xác định tọa độ chính xác |
| 🖐️ **Điều Khiển Máy Tính** | Move mouse, click, gõ chữ, nhấn phím tắt, scroll, drag & drop |
| 🔄 **OODA Loop** | Lặp lại: Observe → Orient → Decide → Act |
| 💾 **Memory System** | Nhớ lịch sử hội thoại và context của task |
| 🌐 **Web Dashboard** | Giao diện web để xem live feed + logs + điều khiển |
| ⚡ **Real-time Updates** | Socket.IO để cập nhật màn hình và logs real-time |
| 🛑 **Safety Features** | Emergency stop ở góc màn hình, rate limiting |
| 📱 **Unicode Support** | Hỗ trợ tiếng Việt, tiếng Trung, v.v. |
| 🎨 **Grid Visualization** | Vẽ lưới tọa độ lên ảnh để AI nhận diện chính xác hơn |

### Supported Actions

```python
# Chuột
- move_mouse(x, y)          # Di chuyển chuột
- left_click(x, y)          # Click trái
- right_click(x, y)         # Click phải
- double_click(x, y)        # Double click
- scroll(direction, amount) # Scroll up/down
- drag_and_drop(x1, y1, x2, y2)  # Kéo thả

# Bàn phím
- type_text("Hello Việt Nam")     # Gõ chữ (Unicode support)
- press_key("a")                  # Nhấn phím đơn
- hotkey("ctrl", "c")             # Phím tắt (Ctrl+C)
- press_key("enter")              # Enter

# Ứng dụng
- open_app("notepad")             # Mở ứng dụng
- open_file("path/to/file.txt")   # Mở file
- open_url("https://example.com") # Mở URL

# Khác
- take_screenshot()    # Chụp ảnh màn hình
- get_screen_info()    # Lấy thông tin màn hình
```

---

## 📦 Yêu Cầu Hệ Thống

### Hệ Điều Hành
- ✅ **Windows** (khuyến nghị)
- ✅ **macOS** 
- ✅ **Linux**

### Phần Mềm
- **Python**: 3.8 trở lên
- **pip**: Package manager của Python

### Phần Cứng
- **RAM**: Tối thiểu 4GB (khuyến nghị 8GB)
- **Internet**: Để kết nối với AI providers (không cần upload dữ liệu lớn)

### Dependencies

```
g4f[all]>=0.4.0                 # AI providers (free)
pyautogui>=0.9.54               # Control mouse/keyboard
pynput>=1.7.6                   # Keyboard input
pillow>=10.0.0                  # Image processing
opencv-python>=4.8.0            # Vision (optional)
mss>=9.0.0                      # Fast screenshots
psutil>=5.9.0                   # System info
colorama>=0.4.6                 # Colored terminal
flask>=3.0.0                    # Web server
flask-socketio>=5.3.0           # Real-time updates
```

---

## 💻 Cài Đặt

### Step 1: Clone Repository

```bash
# Clone project
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use

# Hoặc tải zip
# https://github.com/yourusername/ai-agent-computer-use/archive/refs/heads/main.zip
```

### Step 2: Tạo Virtual Environment (Khuyến nghị)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Cài Đặt Dependencies

```bash
# Cài đặt tất cả packages
pip install -r requirements.txt

# Hoặc cài từng package
pip install g4f[all] pyautogui pynput pillow opencv-python mss psutil colorama flask flask-socketio
```

### Step 4: Cấu Hình Ban Đầu (Tuỳ Chọn)

```bash
# Chỉnh sửa config.py
# - Thiết lập độ phân giải màn hình
# - Thiết lập provider ưu tiên
# - Tùy chỉnh timing, delays, v.v.

nano config.py   # hoặc dùng editor yêu thích
```

### Step 5: Kiểm Tra Cài Đặt

```bash
# Test import G4F
python -c "import g4f; print('✓ G4F OK')"

# Test import other packages
python -c "import pyautogui, pynput, PIL; print('✓ All OK')"
```

---

## 🎮 Cách Dùng

### Chạy Agent (Terminal Mode)

```bash
# Kích hoạt virtual environment (nếu chưa)
.venv\Scripts\activate   # Windows
# hoặc
source .venv/bin/activate  # macOS/Linux

# Chạy agent
python main.py

# Agent sẽ hỏi:
# "Bạn muốn tôi làm gì?"
# Nhập tác vụ của bạn, ví dụ:
# "Mở notepad và viết 'Hello World' rồi lưu lại"
```

### Chạy Dashboard Web

```bash
# Terminal 1: Chạy agent
python main.py

# Terminal 2 (tại cùng folder): Chạy server
python server.py

# Mở trình duyệt: http://localhost:5000
# Nhìn live feed + logs + điều khiển start/stop
```

### Quick Start Script

```bash
# Windows - Chạy `start_dashboard.bat`
# hoặc chạy:
python server.py
```

### Dừng Agent

**3 cách dừng:**

1. **Nhấn `Ctrl+C`** trong terminal
2. **Di chuột vào góc trên bên trái** màn hình (Emergency Stop)
3. **Click nút STOP** trên web dashboard

---

## 🔧 Ví Dụ Thực Tế

### Ví Dụ 1: Tìm Kiếm Thông Tin

```bash
# Task: Mở Google, tìm "Top 10 AI tools 2024" rồi lưu kết quả

$ python main.py

🤖 AI Agent initialized
➜ Bạn muốn tôi làm gì?
> Mở Google Chrome, tìm "Top 10 AI tools 2024" rồi lưu screenshot

[Agent chukp ảnh → Phân tích → Thực hiện]

Step 1: Tìm icon Chrome → Click → Chờ mở
Step 2: Click vào search bar → Gõ "Top 10 AI tools 2024" → Nhấn Enter
Step 3: Chụp ảnh kết quả → Lưu vào screenshots/
Step 4: Quay lại yêu cầu "Hoàn thành!"
```

### Ví Dụ 2: Tự Động Hóa Công Việc Văn Phòng

```bash
# Task: Lấy dữ liệu từ Excel, làm mail merge

$ python main.py

🤖 AI Agent initialized
➜ Bạn muốn tôi làm gì?
> Mở Excel file "data.xlsx", copy danh sách email, mở Gmail draft mail template rồi send test mail

[Agent thực hiện tự động]

✓ Opened Excel
✓ Extracted emails: [abc@gmail.com, def@gmail.com, ...]
✓ Opened Gmail
✓ Composed and sent test emails
✓ Task completed!
```

### Ví Dụ 3: Web Scraping & Data Processing

```bash
# Task: Lấy danh sách sản phẩm từ website

$ python main.py

🤖 AI Agent initialized
➜ Bạn muốn tôi làm gì?
> Vào trang Shopee, tìm "laptop", scroll xuống 5 lần, screenshot các sản phẩm

[Agent tự động]

Step 1: Mở Shopee
Step 2: Tìm kiếm "laptop"
Step 3-7: Scroll và capture
Step 8: Lưu tất cả screenshots
✓ Complete!
```

### Ví Dụ 4: Testing & QA Automation

```bash
# Task: Test login flow của website

$ python main.py

🤖 AI Agent initialized
➜ Bạn muốn tôi làm gì?
> Vào localhost:3000, nhập email "test@example.com", mật khẩu "Test123!", nhấn login, check xem có lỗi không

[Agent tự động test]

✓ Navigated to localhost:3000
✓ Entered email
✓ Entered password
✓ Clicked login button
✓ Captured result screenshot
Result: Login successful ✓
```

---

## 🏗️ Kiến Trúc

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      MAIN LOOP (main.py)                        │
│                                                                 │
│  User Input → Brain → Vision → Actions → Screenshot → Repeat   │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│                    BRAIN (brain.py)                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ G4F Client → Provider Selection → Message Routing      │   │
│  │ - Try Provider 1 (e.g., Claude)                        │   │
│  │ - Fallback to Provider 2 (e.g., GPT-4Free)            │   │
│  │ - Parse JSON response                                  │   │
│  │ - Extract: thought + action                            │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│                   VISION (vision.py)                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Screenshot Capture (MSS) → Grid Draw → Encode to B64  │   │
│  │ - Use MSS (10x faster than pyautogui)                 │   │
│  │ - Draw 16x10 grid overlay                             │   │
│  │ - Label each cell (A1-P10)                            │   │
│  │ - Encode to base64 for AI                             │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│                  ACTIONS (actions.py)                           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Parse & Execute Actions from AI response              │   │
│  │ - click(x, y)                                          │   │
│  │ - type("text")                                         │   │
│  │ - hotkey("ctrl", "a")                                 │   │
│  │ - scroll / drag_and_drop                              │   │
│  │ - open_app / open_url                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│               WEB DASHBOARD (server.py)                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Flask + Socket.IO → Real-time Updates                 │   │
│  │ - Live screen feed                                    │   │
│  │ - Action logs                                         │   │
│  │ - Task status                                         │   │
│  │ - Start/Stop controls                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Module Breakdown

| Module | Trách Nhiệm | Phụ Thuộc |
|--------|-----------|----------|
| **main.py** | Vòng lặp chính, điều phối | brain, vision, actions, config |
| **brain.py** | AI reasoning, G4F integration | g4f, vision |
| **vision.py** | Screenshot, grid, image processing | PIL, MSS, psutil |
| **actions.py** | Mouse, keyboard, app control | pyautogui, pynput |
| **server.py** | Web dashboard, Socket.IO | flask, flask-socketio |
| **config.py** | Global configuration | - |

---

## ⚙️ Cấu Hình Chi Tiết

### Tệp config.py

```python
# ============================================================
# SCREEN - Độ phân giải màn hình
# ============================================================
SCREEN_WIDTH = 1920        # Điều chỉnh theo máy của bạn
SCREEN_HEIGHT = 1080

# ============================================================
# SAFETY - An toàn
# ============================================================
pyautogui.FAILSAFE = True  # Di chuột vào góc để dừng
MAX_STEPS = 30             # Số bước tối đa mỗi task
STEP_DELAY = 12.0          # Chờ 12s giữa các bước (tránh rate limit)
SHOW_OVERLAY = False       # Hiển thị UI overlay

# ============================================================
# MOUSE - Tùy chỉnh chuột
# ============================================================
MOUSE_MOVE_DURATION = 0.4  # Thời gian di chuyển (giây)
HUMAN_LIKE_MOUSE = True    # Di chuột theo đường cong tự nhiên

# ============================================================
# KEYBOARD - Tùy chỉnh bàn phím
# ============================================================
TYPE_INTERVAL = 0.04       # Khoảng cách giữa các phím
TYPE_DELAY_AFTER = 0.3     # Delay sau khi gõ xong

# ============================================================
# VISION - Thị giác
# ============================================================
GRID_ENABLED = True        # Vẽ grid hay không
GRID_ROWS = 10             # Số hàng (mặc định 10)
GRID_COLS = 16             # Số cột (mặc định 16)
GRID_COLOR = (0, 255, 0)   # Màu (BGR - xanh lá)
GRID_ALPHA = 0.15          # Độ trong suốt

# ============================================================
# AI BRAIN - Bộ não
# ============================================================
PREFERRED_PROVIDERS = [
    "claude",              # Thử Claude trước
    "gpt-4-free",
    "openai",
]

MAX_RETRIES = 3            # Thử lại tối đa 3 lần nếu lỗi
TIMEOUT = 30               # Timeout 30 giây

# ============================================================
# LOGGING
# ============================================================
LOG_LEVEL = "INFO"         # DEBUG, INFO, WARNING, ERROR
SAVE_SCREENSHOTS = True    # Lưu screenshot tự động
SCREENSHOT_DIR = "screenshots"

# ============================================================
# VOICE (Tuỳ chọn)
# ============================================================
USE_VOICE_INPUT = False    # Dùng voice command hay không
VOICE_LANGUAGE = "vi"      # Tiếng Việt
```

### Cấu Hình cho Các Provider AI

```python
# Trong brain.py - tuỳ chỉnh providers

PROVIDER_CONFIG = {
    "claude": {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 2000,
    },
    "gpt-4-free": {
        "model": "gpt-4",
        "temperature": 0.7,
    },
    "openai": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
    },
}
```

### Environment Variables (Tuỳ chọn)

```bash
# .env file (nếu cần)
export G4F_TIMEOUT=30
export G4F_MAX_RETRIES=3
export AI_LOG_LEVEL=DEBUG
export SCREENSHOT_QUALITY=90
```

---

## 🌐 Web Dashboard

### Tính Năng Dashboard

#### 1. Live Screen Feed
- Xem video live của màn hình máy (cập nhật mỗi 2 giây)
- Hiển thị grid overlay
- Đánh dấu vị trí chuột hiện tại

#### 2. Action Logger
- Xem mọi hành động của agent real-time
- Timestamps cho mỗi hành động
- Color-coded: success (xanh), warning (vàng), error (đỏ)

#### 3. Thought Process
- Xem suy nghĩ của AI trước khi hành động
- Xem output JSON từ AI
- Debug mode để xem raw response

#### 4. Task Control
- **START** button: Bắt đầu task mới
- **STOP** button: Dừng task hiện tại
- **RESTART** button: Restart agent

#### 5. Statistics
- Số bước thực hiện
- Thời gian chạy
- Số nhà cung cấp AI được thử
- Success/failure rate

### Chạy Dashboard

```bash
# Terminal 1: Agent
python main.py

# Terminal 2: Dashboard
python server.py

# Trình duyệt
open http://localhost:5000
```

### Cấu Hình Dashboard

```python
# Trong server.py
DASHBOARD_PORT = 5000           # Port mặc định
DASHBOARD_HOST = "0.0.0.0"      # Listen trên tất cả interfaces
DEBUG_MODE = False              # Production mode
MAX_LOGS = 1000                 # Giữ 1000 logs cuối cùng
SCREENSHOT_QUALITY = 85         # Compression quality
```

---

## 📡 API Reference

### G4F Integration

```python
from g4f.client import Client

client = Client()

# Cách dùng cơ bản
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ],
    stream=False,
)

text = response.choices[0].message.content
```

### Vision API

```python
from vision import Vision

vision = Vision()

# Chụp ảnh
img = vision.capture_screen()

# Vẽ grid
img_with_grid = vision.draw_grid(img)

# Encode thành base64 (cho AI)
img_b64 = vision.encode_base64(img)
```

### Actions API

```python
from actions import Actions

actions = Actions()

# Chuột
actions.move_mouse(100, 200)
actions.left_click(500, 300)
actions.double_click(600, 400)
actions.scroll("down", 3)

# Bàn phím
actions.type_text("Hello Việt Nam")
actions.press_key("enter")
actions.hotkey("ctrl", "c")

# Ứng dụng
actions.open_app("notepad")
actions.open_url("https://google.com")
```

### Brain API

```python
from brain import Brain

brain = Brain()

# Phân tích ảnh + trả về action
action = brain.analyze_and_decide(
    screenshot_base64,
    task_description,
    history=[]
)

# Result: {"thought": "...", "action": {...}}
```

---

## 🛡️ Lưu Ý An Toàn

### Safety Features

1. **Emergency Stop (Failsafe)**
   - Di chuột vào góc trên bên trái → Agent dừng ngay
   - Thiết lập: `config.EMERGENCY_STOP_CORNER_SIZE`

2. **Rate Limiting**
   - Delay 12 giây giữa các bước (tránh quá tải server AI)
   - Thiết lập: `config.STEP_DELAY`

3. **Max Steps**
   - Tối đa 30 bước mỗi task (tránh vòng lặp vô hạn)
   - Thiết lập: `config.MAX_STEPS`

4. **Timeout**
   - Mỗi AI call có timeout 30 giây
   - Nếu timeout → Thử provider khác

### Best Practices

```bash
# ✅ LÀM
- Chạy trên máy ảo/ container để test
- Backup dữ liệu quan trọng trước khi chạy
- Monitor dashboard để theo dõi hành động
- Bắt đầu với tasks đơn giản

# ❌ KHÔNG LÀM
- Chạy trên máy production chính
- Để agent chạy không giám sát quá lâu
- Cho agent full control trên sensitive areas
- Chạy nhiều agent cùng lúc trên cùng máy
```

### Permissions & Sandboxing

```bash
# Trên Linux - Chạy agent trong container
docker run -it --rm --display=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  ai-agent-computer-use

# Hoặc dùng virtual machine
# VirtualBox → Tạo VM → Cài Python → Chạy agent
```

### Logging & Monitoring

```python
# Bật debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Hoặc thay đổi config
config.LOG_LEVEL = "DEBUG"

# Xem logs
tail -f agent.log
```

---

## 🔧 Xử Lý Sự Cố

### Vấn Đề: Agent không kết nối được G4F

**Triệu chứng:**
```
❌ Error: Failed to connect to G4F providers
```

**Giải pháp:**
```bash
# 1. Kiểm tra internet
ping 8.8.8.8

# 2. Cập nhật G4F
pip install --upgrade g4f

# 3. Kiểm tra providers khả dụng
python -c "from g4f.client import Client; c = Client(); print(c.providers)"

# 4. Thay đổi provider ưu tiên
# Trong config.py, đổi PREFERRED_PROVIDERS
```

### Vấn Đề: Agent click nhầm vị trí

**Triệu chứng:**
```
Chuột click vào vị trí sai, không nhắm trúng button
```

**Giải pháp:**
```bash
# 1. Bật SHOW_OVERLAY để xem grid
config.SHOW_OVERLAY = True

# 2. Kiểm tra độ phân giải
config.SCREEN_WIDTH = 1920   # Điều chỉnh theo máy
config.SCREEN_HEIGHT = 1080

# 3. Tăng độ chính xác grid
config.GRID_ROWS = 12        # Mặc định 10
config.GRID_COLS = 18        # Mặc định 16

# 4. Test manual
python test_vision.py
```

### Vấn Đề: Screenshot bị giật/ lag

**Triệu chứng:**
```
FPS thấp, screenshot chậm, dashboard lag
```

**Giải pháp:**
```python
# config.py
STEP_DELAY = 5.0           # Giảm delay xuống
SCREENSHOT_QUALITY = 70    # Giảm quality để nhanh hơn
GRID_ENABLED = False       # Tắt grid để lưu tài nguyên

# Hoặc dùng daemon mode (background)
nohup python main.py &
```

### Vấn Đề: Gõ chữ tiếng Việt bị lỗi

**Triệu chứng:**
```
Gõ "Xin chào" bị thành gibberish
```

**Giải pháp:**
```python
# actions.py - đã support Unicode
# Nhưng nếu vẫn lỗi:

# 1. Windows - thiết lập locale
import locale
locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

# 2. macOS - không cần gì thêm

# 3. Linux - cài input method
sudo apt-get install ibus ibus-unikey
```

### Vấn Đề: Dashboard không hiển thị

**Triệu chứng:**
```
Mở http://localhost:5000 nhưng trống hoặc error
```

**Giải pháp:**
```bash
# 1. Kiểm tra port đã được dùng hay chưa
netstat -an | grep 5000    # macOS/Linux
netstat -ano | findstr 5000 # Windows

# 2. Đổi port khác
# Trong server.py
app.run(port=8000, debug=False)

# 3. Kiểm tra Flask cài đặt
pip install --upgrade flask flask-socketio

# 4. Xem logs
python server.py --debug
```

### Vấn Đề: Provider G4F nói "Too many requests"

**Triệu chứng:**
```
Error: Rate limit exceeded
```

**Giải pháp:**
```python
# config.py - tăng delay
STEP_DELAY = 20.0      # Từ 12 lên 20 giây

# Hoặc đợi và thử lại
# Một số provider có limit ~5 requests/minute
```

### Vấn Đề: Agent stuck/ loop vô hạn

**Triệu chứng:**
```
Agent thực hiện cùng một hành động liên tục
```

**Giải pháp:**
```bash
# 1. Nhấn Ctrl+C để dừng
# 2. Di chuột vào góc trên trái (Emergency Stop)
# 3. Xem logs để tìm nguyên nhân
# 4. Điều chỉnh MAX_STEPS
config.MAX_STEPS = 15      # Giảm xuống để terminate sớm
```

### Vấn Đề: Máy chậm khi chạy agent

**Triệu chứng:**
```
CPU, RAM chạy full, máy lag
```

**Giải pháp:**
```python
# config.py - tối ưu
SCREENSHOT_QUALITY = 50      # Giảm chất lượng
GRID_ENABLED = False         # Tắt grid
STEP_DELAY = 5.0            # Tăng delay (ít request hơn)

# Hoặc chạy trên máy khác/ container
docker run --cpus=2 --memory=2g ai-agent
```

---

## 🤝 Đóng Góp

Chúng tôi rất hoan nghênh các đóng góp từ cộng đồng! 

### Cách Đóng Góp

1. **Fork** repository
2. **Tạo branch** cho feature của bạn
   ```bash
   git checkout -b feature/awesome-feature
   ```
3. **Commit** thay đổi
   ```bash
   git commit -m "Add awesome feature"
   ```
4. **Push** lên branch
   ```bash
   git push origin feature/awesome-feature
   ```
5. **Mở Pull Request**

### Hướng Dẫn Phát Triển

```bash
# Clone repo
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use

# Tạo virtual env
python -m venv .venv
source .venv/bin/activate  # hoặc .venv\Scripts\activate

# Cài dependencies (bao gồm dev dependencies)
pip install -r requirements.txt -r requirements-dev.txt

# Chạy tests
pytest tests/

# Chạy linting
flake8 .
black .

# Chạy agent
python main.py
```

### Ideas để Đóng Góp

- 🔨 **Bug fixes** - Tìm và sửa bugs
- ✨ **New features**:
  - Voice control (text-to-speech)
  - Multi-screen support
  - Plugin system
  - OCR integration
  - Browser automation (Selenium)
- 📚 **Documentation** - Thêm ví dụ, hướng dẫn
- 🧪 **Tests** - Viết unit tests, integration tests
- 🌐 **Translations** - Dịch sang ngôn ngữ khác
- 🎨 **UI/UX** - Cải thiện dashboard

### Code Standards

```python
# PEP 8 style guide
# Type hints when possible
# Docstrings cho functions

def analyze_screen(screenshot: Image.Image) -> dict:
    """
    Phân tích ảnh màn hình bằng AI.
    
    Args:
        screenshot: PIL Image object
        
    Returns:
        dict: {"thought": str, "action": dict}
    """
    pass
```

### Pull Request Template

```markdown
## Description
Mô tả thay đổi của bạn

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation

## Testing
Cách test thay đổi này?

## Checklist
- [ ] Đã test trên Windows
- [ ] Đã test trên macOS/Linux
- [ ] Đã update documentation
- [ ] Không có breaking changes
```

---

## 📝 License

Dự án này được phân phối dưới **MIT License** — tự do sử dụng, sửa đổi, phân phối.

```
MIT License

Copyright (c) 2024 AI Agent Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 📞 Contact & Support

### Liên Hệ

- **GitHub Issues**: [Report bugs here](https://github.com/yourusername/ai-agent-computer-use/issues)
- **Discussions**: [Ask questions](https://github.com/yourusername/ai-agent-computer-use/discussions)
- **Email**: your-email@example.com

### Community

- 🌟 **Star** repo nếu thích project
- 📢 **Share** với bạn bè
- 💬 **Join** discussions
- 🐛 **Report bugs** để giúp cải thiện

### Roadmap

- [x] Core agent loop
- [x] G4F integration
- [x] Vision module
- [x] Web dashboard
- [ ] Voice control
- [ ] Plugin system
- [ ] Multi-agent support
- [ ] Advanced memory system
- [ ] Custom model support
- [ ] Mobile app

---

## 🎓 Học Thêm

### Tài Liệu
- [G4F Documentation](https://github.com/xtekky/gpt4free)
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Các Dự Án Tương Tự
- [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT)
- [Agent.py](https://github.com/minimaxir/agent-py)
- [Anthropic Claude API](https://www.anthropic.com/)

### Blog Posts & Tutorials
- Coming soon...

---

## 🎉 Cảm Ơn

Cảm ơn tất cả những người đã đóng góp, báo cáo bugs, và hỗ trợ dự án này!

---

<div align="center">

**Made with ❤️ by AI Agent Contributors**

*Giúp máy tính bạn tự động hóa, tự do hơn.*

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ai-agent-computer-use?style=social)](https://github.com/yourusername/ai-agent-computer-use)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/ai-agent-computer-use?style=social)](https://github.com/yourusername/ai-agent-computer-use)

</div>
