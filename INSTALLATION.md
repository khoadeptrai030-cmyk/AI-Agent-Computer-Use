# 🚀 Hướng Dẫn Cài Đặt Chi Tiết

## 📋 Mục Lục
1. [Windows](#-windows)
2. [macOS](#-macos)
3. [Linux](#-linux)
4. [Docker](#-docker)
5. [Kiểm Tra Cài Đặt](#-kiểm-tra-cài-đặt)

---

## 💻 Windows

### Bước 1: Tải Python

1. Vào [python.org](https://www.python.org/downloads/)
2. Tải **Python 3.11** trở lên (khuyến nghị)
3. **Quan trọng**: ✅ Tick "Add Python to PATH" khi cài

Kiểm tra:
```bash
python --version
# Output: Python 3.11.x
```

### Bước 2: Clone Project

```bash
# Vào folder bạn muốn
cd D:\MyProjects

# Clone repository
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use
```

Hoặc tải ZIP:
- Vào [GitHub](https://github.com/yourusername/ai-agent-computer-use)
- Click **Code** → **Download ZIP**
- Giải nén

### Bước 3: Tạo Virtual Environment

```bash
# Tạo venv
python -m venv .venv

# Kích hoạt (lưu ý: dấu backslash và ".bat")
.venv\Scripts\activate.bat

# Hoặc PowerShell
.venv\Scripts\Activate.ps1

# Nếu gặp lỗi PowerShell:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

**Kiểm tra**: Prompt terminal sẽ hiện `(.venv)` ở đầu

### Bước 4: Cài Dependencies

```bash
# Đảm bảo đang ở trong venv (.venv)
pip install --upgrade pip

# Cài tất cả
pip install -r requirements.txt

# Nếu lỗi, cài từng cái:
pip install g4f[all]
pip install pyautogui
pip install pynput
pip install pillow
pip install opencv-python
pip install mss
pip install psutil
pip install colorama
pip install flask
pip install flask-socketio
```

### Bước 5: Chạy Agent

```bash
# Đảm bảo venv đang active (.venv)
python main.py

# Hoặc chạy dashboard
python server.py
# Mở: http://localhost:5000
```

### Gỡ Cài (Uninstall)

```bash
# Xóa venv
rmdir /s .venv

# Hoặc xóa folder project
rm -r ai-agent-computer-use
```

---

## 🍎 macOS

### Bước 1: Kiểm Tra Python

```bash
# macOS thường có Python sẵn, nhưng có thể cũ
python3 --version

# Nếu cần Python mới, dùng Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.11
```

### Bước 2: Clone Project

```bash
cd ~/Desktop
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use
```

### Bước 3: Tạo Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate

# Nếu dùng zsh shell (mặc định trên macOS mới):
# source .venv/bin/activate
# sẽ tự hoạt động
```

### Bước 4: Cài Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Lưu ý macOS**: Một số packages có thể cần xcode-select

```bash
xcode-select --install  # Nếu chưa cài
```

### Bước 5: Cấp Quyền Accessibility (Quan Trọng!)

Để PyAutoGUI có thể control mouse/keyboard:

1. **System Preferences** → **Security & Privacy**
2. **Privacy** tab (bên trái)
3. **Accessibility** → **+**
4. Chọn **Terminal** (hoặc IDE bạn dùng)
5. Restart Terminal

```bash
# Hoặc command line
sudo sqlite3 /Library/Application\ Support/com.apple.sharedfilelist add-domain '/Library/Application\ Support/CrashReporter/.symlinks' 'com.apple.trust-settings' 'admin' '/usr/local/bin/python3' 1
```

### Bước 6: Chạy

```bash
source .venv/bin/activate  # Kích hoạt venv
python main.py
```

### Fix Vấn Đề Chuột Không Hoạt động

```python
# Trong main.py hoặc config.py, thêm:
import os
os.environ['PYOBJC_FRAMEWORK_BRIDGE'] = '1'
```

---

## 🐧 Linux

### Bước 1: Cài Python & pip

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

**Fedora/RHEL:**
```bash
sudo dnf install python3 python3-pip
```

**Arch:**
```bash
sudo pacman -S python python-pip
```

### Bước 2: Cài Dependencies Hệ Thống

Cần một số package để hỗ trợ automation & image processing:

**Ubuntu/Debian:**
```bash
sudo apt-get install \
    xdotool \
    python3-tk \
    libopencv-dev \
    python3-opencv \
    libssl-dev \
    libffi-dev
```

**Fedora:**
```bash
sudo dnf install \
    xdotool \
    python3-tkinter \
    opencv-devel \
    python3-devel
```

### Bước 3: Clone & Setup Venv

```bash
cd ~/projects
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use

python3 -m venv .venv
source .venv/bin/activate
```

### Bước 4: Cài Python Packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Nếu lỗi với opencv:
```bash
pip install opencv-python-headless  # thay vì opencv-python
```

### Bước 5: Cấp Quyền Input Device

Để control mouse/keyboard, cần quyền:

```bash
# Thêm user vào input group
sudo usermod -a -G input $USER

# Hoặc chạy với sudo (không khuyến nghị)
sudo python main.py

# Logout/login hoặc restart
```

### Bước 6: Chạy

```bash
source .venv/bin/activate
python main.py
```

### Sử Dụng X11 Display (Nếu Dùng Headless)

```bash
# Set DISPLAY variable
export DISPLAY=:0
python main.py

# Hoặc trong script
DISPLAY=:0 python main.py
```

---

## 🐳 Docker

### Cách 1: Dockerfile (Build Mới)

**Tạo file `Dockerfile`:**

```dockerfile
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    xdotool python3-tk \
    opencv-python-headless \
    libssl-dev libffi-dev \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project
COPY . .

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set display
ENV DISPLAY=:0

# Run agent
CMD ["python", "main.py"]
```

**Build & chạy:**

```bash
# Build image
docker build -t ai-agent .

# Chạy container (với X11 forwarding)
docker run -it --rm \
    --display=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd):/app \
    ai-agent

# Hoặc chạy dashboard
docker run -it --rm \
    -p 5000:5000 \
    -v $(pwd):/app \
    ai-agent python server.py
```

### Cách 2: Docker Compose

**Tạo `docker-compose.yml`:**

```yaml
version: '3.8'

services:
  agent:
    build: .
    container_name: ai-agent
    environment:
      - DISPLAY=${DISPLAY}
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix
      - .:/app
      - ./screenshots:/app/screenshots
    ports:
      - "5000:5000"
    stdin_open: true
    tty: true
```

**Chạy:**

```bash
docker-compose up --build
```

---

## ✅ Kiểm Tra Cài Đặt

Sau khi cài đặt, chạy tests:

### Test 1: Import Packages

```bash
# Kích hoạt venv
source .venv/bin/activate  # Linux/macOS
# hoặc
.venv\Scripts\activate  # Windows

# Test imports
python -c "
import g4f
import pyautogui
import pynput
import PIL
import mss
import psutil
import flask
print('✓ All imports OK')
"
```

### Test 2: Chạy Unit Tests

```bash
python -m pytest tests/ -v

# Hoặc
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test 3: Test Vision Module

```bash
python test_vision.py
# Sẽ chụp 5 ảnh màn hình, lưu vào screenshots/
```

### Test 4: Test Brain Module

```bash
python test_brain.py
# Sẽ test kết nối G4F + parsing response
```

### Test 5: Test Manual

```bash
# Chạy với debug
python main.py --debug

# Hoặc
LOG_LEVEL=DEBUG python main.py
```

---

## 🎯 Quick Start (Tl;dr)

### Windows
```bash
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### macOS/Linux
```bash
git clone https://github.com/yourusername/ai-agent-computer-use.git
cd ai-agent-computer-use
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🆘 Gặp Vấn Đề?

- **❌ "No module named 'g4f'"** → Chạy `pip install g4f[all]`
- **❌ "Permission denied"** → Dùng `sudo` hoặc fix permissions
- **❌ "Screen capture failed"** → Kiểm tra DISPLAY (Linux) hoặc resolution (config.py)
- **❌ "Port 5000 already in use"** → Đổi port trong server.py

Xem [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) để fix chi tiết!
