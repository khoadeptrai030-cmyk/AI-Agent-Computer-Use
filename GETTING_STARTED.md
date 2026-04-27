# 🎯 Bắt Đầu Nhanh (Quick Start)

Hướng dẫn 5 phút để bắt đầu sử dụng AI Agent.

---

## ⚡ 5 Phút Setup

### Step 1: Yêu Cầu (30 giây)

- **OS**: Windows, macOS, hoặc Linux
- **Python**: 3.8+ ([Download](https://python.org))
- **Git**: (optional, để clone repo)
- **Internet**: Để kết nối AI providers

### Step 2: Clone & Setup (2 phút)

```bash
# Clone project
git clone https://github.com/khoadeptrai030-cmyk/ai-agent-computer-use.git
cd ai-agent-computer-use

# Tạo virtual environment
python -m venv .venv

# Kích hoạt (chọn một trong hai)
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Cài dependencies
pip install -r requirements.txt
```

### Step 3: Test (1 phút)

```bash
# Kiểm tra cài đặt
python -c "import g4f, pyautogui; print('✓ OK')"

# Chạy agent đầu tiên
python main.py
```

### Step 4: Chạy Dashboard (optional, 1 phút)

```bash
# Terminal khác (vẫn ở folder project, venv active)
python server.py

# Mở: http://localhost:5000
```

---

## 📝 First Task

### Ví Dụ 1: Tìm Kiếm Google (Ngắn nhất)

```bash
$ python main.py

🤖 AI Agent initialized. OODA loop started.

🎯 What do you want me to do?
> Mở Google tìm "Python tutorial" rồi cho tôi 3 link đầu tiên

[Agent chụp ảnh, phân tích, và thực hiện...]

⏱️  Step 1/5: Taking screenshot...
⏱️  Step 2/5: Analyzing with AI...
⏱️  Step 3/5: Opening Google...
⏱️  Step 4/5: Searching...
⏱️  Step 5/5: Extracting results...

📋 Found 3 links:
1. https://www.python.org/about/gettingstarted/
2. https://docs.python.org/3/tutorial/
3. https://www.w3schools.com/python/

✅ Task completed!
```

### Ví Dụ 2: Tạo File Văn Bản (Bình thường)

```bash
$ python main.py

🎯 What do you want me to do?
> Mở Notepad, viết "Hello AI Agent", lưu file thành "greeting.txt"

[Agent thực hiện...]

✅ File saved: greeting.txt
```

### Ví Dụ 3: Tự Động Hóa (Nâng cao)

```bash
$ python main.py

🎯 What do you want me to do?
> Mở Excel, import file "data.csv", tạo biểu đồ, save thành PDF

[Agent thực hiện tự động...]

✅ PDF saved: report.pdf
```

---

## 🎮 Điều Khiển Agent

### Trong Terminal

- **Gõ yêu cầu**: Nhập tác vụ bạn muốn
- **Dừng:** `Ctrl+C`
- **Xem logs**: Tự động in ra terminal

### Cách Dừng Khẩn Cấp

1. **Di chuột vào góc trên bên trái** màn hình
2. **Click nút STOP** trên web dashboard (nếu chạy server)
3. **Nhấn `Ctrl+C`** trong terminal

### Trên Web Dashboard

```
http://localhost:5000
```

**Các tính năng:**
- 📺 Xem live screen feed
- 📝 Xem action logs real-time
- 🎮 Nút START/STOP
- 💭 Xem suy nghĩ của AI

---

## ⚙️ Cấu Hình Cơ Bản

**File: `config.py`**

Các thông số quan trọng:

```python
# Độ phân giải màn hình (chỉnh theo máy)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# An toàn
MAX_STEPS = 30              # Tối đa 30 bước mỗi task
STEP_DELAY = 12.0           # Chờ 12 giây giữa các bước (tránh rate limit)

# Hiển thị grid tọa độ
GRID_ENABLED = True

# Dashboard web
DASHBOARD_PORT = 5000
```

---

## 🆘 Vấn Đề Thường Gặp

### ❌ "No module named 'g4f'"

```bash
pip install g4f[all]
```

### ❌ Agent click nhầm vị trí

**Nguyên nhân**: Độ phân giải không khớp

**Fix:**
1. Check độ phân giải thực tế
2. Chỉnh trong `config.py`:
```python
SCREEN_WIDTH = 1920   # Thay đúng kích thước
SCREEN_HEIGHT = 1080
```

### ❌ "Failed to connect to G4F"

**Nguyên nhân**: Mất internet hoặc provider bị chặn

**Fix:**
```bash
# Kiểm tra internet
ping 8.8.8.8

# Cập nhật G4F
pip install --upgrade g4f
```

### ❌ Dashboard không hiển thị

**Nguyên nhân**: Port 5000 đang dùng

**Fix:**
```bash
# Kiểm tra
netstat -an | grep 5000

# Đổi port (trong server.py)
app.run(port=8000, debug=False)

# Hoặc kill process
kill -9 $(lsof -ti:5000)
```

### ❌ Gõ chữ tiếng Việt bị lỗi

**Fix**: Đã support Unicode. Nếu vẫn lỗi:

```python
# Trong config.py
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

---

## 📚 Tài Liệu Chi Tiết

| Tài Liệu | Nội Dung |
|---------|---------|
| [README.md](./README.md) | Giới thiệu toàn diện, tính năng, API |
| [INSTALLATION.md](./INSTALLATION.md) | Hướng dẫn cài đặt từng OS |
| [EXAMPLES.md](./EXAMPLES.md) | 20+ ví dụ thực tế |
| [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Fix lỗi chi tiết |

---

## 🎯 Bước Tiếp Theo

### Sau khi setup thành công:

1. **Chạy vài ví dụ**
   ```bash
   python main.py
   # Thử: "Mở Notepad"
   # Thử: "Mở Chrome"
   # Thử: "Tìm Google"
   ```

2. **Explore codebase**
   - Đọc `main.py` để hiểu vòng lặp
   - Đọc `brain.py` để hiểu AI
   - Đọc `actions.py` để xem actions có sẵn

3. **Tùy chỉnh config**
   - Chỉnh độ phân giải
   - Chỉnh delays nếu quá chậm
   - Bật/tắt features

4. **Tạo task custom**
   - Viết script riêng
   - Combine nhiều actions
   - Export kết quả

5. **Tham gia cộng đồng**
   - Star ⭐ repo
   - Report bugs
   - Gợi ý features

---

## 🚀 Production Use

### Để chạy 24/7:

```bash
# Linux/macOS - Background process
nohup python main.py > agent.log 2>&1 &

# Windows - Task Scheduler
# Tạo task chạy: python main.py

# Hoặc dùng Docker
docker-compose up -d
```

### Logging & Monitoring

```python
# config.py
LOG_LEVEL = "INFO"  # hoặc "DEBUG"

# Xem logs
tail -f agent.log

# Hoặc trên web dashboard
# http://localhost:5000
```

---

## 💡 Pro Tips

1. **Test trước**: Luôn test task trên "máy ảo" trước
2. **Gradual rollout**: Bắt đầu với tasks đơn giản
3. **Monitor**: Luôn giám sát agent khi chạy
4. **Backup**: Backup dữ liệu quan trọng trước khi chạy
5. **Rate limit**: Để delay đủ lớn để tránh rate limit

---

## ❓ FAQ

**Q: Agent có thể làm gì?**
A: Bất cứ điều gì bạn làm thủ công trên máy tính: click, gõ, mở app, v.v.

**Q: Có an toàn không?**
A: Có emergency stop ở góc màn hình + rate limiting + max steps limit

**Q: Làm sao dừng agent?**
A: Ctrl+C, emergency stop ở góc, hoặc nút STOP trên dashboard

**Q: Cần API key không?**
A: Không! Dùng G4F (free providers)

**Q: Hoạt động offline không?**
A: Không, cần internet để kết nối AI providers

**Q: Chạy được trên Mac không?**
A: Có, nhưng cần cấp permission accessibility cho terminal

**Q: Hỗ trợ tiếng Việt không?**
A: Có! Gõ câu lệnh bằng tiếng Việt cũng được

**Q: Làm sao tùy chỉnh?**
A: Chỉnh `config.py`, hoặc viết custom script dùng `brain.py` / `actions.py`

---

## 📞 Cần Giúp?

- 📖 Đọc [README.md](./README.md)
- 🔧 Xem [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
- 📚 Xem [EXAMPLES.md](./EXAMPLES.md)
- 🐛 [Report bug](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues)
- 💬 [Join discussions](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/discussions/1)

---

## 🎉 Bạn Đã Sẵn Sàng!

```
✓ Python cài đặt
✓ Dependencies cài đặt
✓ Config hoàn tất
✓ Sẵn sàng chạy

Hãy: python main.py

Enjoy! 🚀
```

---

**Happy Automating! 🎯**
