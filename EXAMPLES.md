# 📚 Ví Dụ Thực Tế & Các Trường Hợp Sử Dụng

## 🎯 Giới Thiệu

Tài liệu này chứa **20+ ví dụ thực tế** cách sử dụng AI Agent để tự động hóa các tác vụ.

---

## 📂 Mục Lục

### Nhóm 1: Web Automation
- [Ví dụ 1: Tìm kiếm Google](#ví-dụ-1-tìm-kiếm-google)
- [Ví dụ 2: Đăng nhập & Scraping](#ví-dụ-2-đăng-nhập-website)
- [Ví dụ 3: Mua hàng online](#ví-dụ-3-mua-hàng-online)

### Nhóm 2: Office Automation
- [Ví dụ 4: Mail merge Excel → Gmail](#ví-dụ-4-mail-merge)
- [Ví dụ 5: Tạo report từ dữ liệu](#ví-dụ-5-tạo-report)
- [Ví dụ 6: Chuyển đổi format tài liệu](#ví-dụ-6-chuyển-đổi-format)

### Nhóm 3: Testing & QA
- [Ví dụ 7: Test login flow](#ví-dụ-7-test-login)
- [Ví dụ 8: Kiểm tra responsive design](#ví-dụ-8-test-responsive)
- [Ví dụ 9: Automation test suite](#ví-dụ-9-test-suite)

### Nhóm 4: Social Media
- [Ví dụ 10: Đăng bài Facebook](#ví-dụ-10-post-facebook)
- [Ví dụ 11: Schedule tweets](#ví-dụ-11-schedule-tweets)
- [Ví dụ 12: Bulk follow Instagram](#ví-dụ-12-bulk-follow)

### Nhóm 5: System Administration
- [Ví dụ 13: Backup files](#ví-dụ-13-backup)
- [Ví dụ 14: Monitor process](#ví-dụ-14-monitor)
- [Ví dụ 15: Batch rename files](#ví-dụ-15-batch-rename)

### Nhóm 6: Data Processing
- [Ví dụ 16: CSV import/export](#ví-dụ-16-csv-import)
- [Ví dụ 17: Format data](#ví-dụ-17-format-data)
- [Ví dụ 18: Merge spreadsheets](#ví-dụ-18-merge-spreadsheets)

### Nhóm 7: Creative & Content
- [Ví dụ 19: Batch image resize](#ví-dụ-19-batch-image)
- [Ví dụ 20: Video thumbnail extraction](#ví-dụ-20-video-thumbnail)

---

## 🌐 Nhóm 1: Web Automation

### Ví Dụ 1: Tìm Kiếm Google

**Yêu cầu:**
```
Tìm "best AI tools 2024" trên Google, lưu 10 kết quả đầu tiên
```

**Cách chạy:**
```bash
python main.py

# Agent sẽ hỏi:
# 🤖: Bạn muốn tôi làm gì?
# > Tìm "best AI tools 2024" trên Google, lưu 10 kết quả đầu tiên

# Agent thực hiện:
# 1. Mở trình duyệt
# 2. Vào google.com
# 3. Click search bar
# 4. Gõ "best AI tools 2024"
# 5. Nhấn Enter
# 6. Chụp ảnh
# 7. Đọc danh sách từ ảnh
# 8. Lưu vào file
```

**Expected Output:**
```
Step 1: Opened Chrome browser
Step 2: Navigated to google.com
Step 3: Clicked search box
Step 4: Typed "best AI tools 2024"
Step 5: Pressed Enter
Step 6: Captured results
Step 7: Extracted links:
  - openai.com
  - anthropic.com
  - ...
✓ Task completed!
```

**Code Manual (nếu muốn tùy chỉnh):**
```python
from brain import Brain
from vision import Vision
from actions import Actions

brain = Brain()
vision = Vision()
actions = Actions()

# 1. Mở trình duyệt
actions.open_url("https://google.com")
actions.wait(3)  # Chờ tải

# 2. Chụp ảnh
img = vision.capture_screen()

# 3. Phân tích (AI sẽ find search box)
prompt = "Click on the Google search box and type 'best AI tools 2024'"
analysis = brain.analyze_and_decide(img, prompt)

# 4. Thực hiện action
if analysis['action']['type'] == 'click':
    actions.left_click(analysis['action']['x'], analysis['action']['y'])
```

---

### Ví Dụ 2: Đăng Nhập Website

**Yêu cầu:**
```
Đăng nhập vào GitHub với email example@gmail.com, mật khẩu MyPassword123
```

**Command:**
```bash
python main.py

# Input:
# > Đăng nhập vào GitHub. Email: example@gmail.com, Password: MyPassword123

# Steps:
# 1. Mở https://github.com/login
# 2. Điền email
# 3. Điền password
# 4. Click "Sign in"
# 5. Kiểm tra xem có 2FA không
# 6. Nếu có, hỏi user nhập OTP
# 7. Dashboard loaded ✓
```

**Lưu ý An Toàn:**
```bash
# KHÔNG bao giờ:
# - Hardcode password vào code
# - Chia sẻ credentials trên GitHub
# - Lưu password dưới dạng plain text

# NÊN:
# - Dùng environment variables
export GITHUB_EMAIL="example@gmail.com"
export GITHUB_PASSWORD="MyPassword123"

# Hoặc .env file (gitignored)
# .env
GITHUB_EMAIL=example@gmail.com
GITHUB_PASSWORD=MyPassword123

# Trong code
import os
email = os.getenv("GITHUB_EMAIL")
password = os.getenv("GITHUB_PASSWORD")
```

---

### Ví Dụ 3: Mua Hàng Online

**Yêu cầu:**
```
Vào Shopee, tìm "laptop under 10 million", chọn sản phẩm đầu tiên, 
thêm vào giỏ hàng, tiến hành checkout
```

**Command:**
```bash
python main.py

# Input:
# > Vào Shopee, tìm "laptop under 10 million", thêm vào giỏ hàng

# Expected flow:
# Step 1: Mở https://shopee.vn
# Step 2: Click search
# Step 3: Gõ "laptop under 10 million"
# Step 4: Nhấn Enter
# Step 5: Chọn sản phẩm đầu tiên (click)
# Step 6: Chụp ảnh chi tiết sản phẩm
# Step 7: Click "Add to cart"
# Step 8: Confirm dialog
# ✓ Added to cart!
```

---

## 💼 Nhóm 2: Office Automation

### Ví Dụ 4: Mail Merge

**Yêu cầu:**
```
Đọc danh sách email từ Excel, gửi email tới mỗi người qua Gmail
```

**File: `examples/mail_merge.py`**

```python
from brain import Brain
from actions import Actions
import pandas as pd
import time

# Bước 1: Đọc file Excel
emails_df = pd.read_excel("contacts.xlsx")
# Format: Name, Email, Company

# Bước 2: Dùng agent để gửi email
actions = Actions()
brain = Brain()

for idx, row in emails_df.iterrows():
    name = row['Name']
    email = row['Email']
    company = row['Company']
    
    # Task cho AI
    task = f"""
    Gửi email tới {email} với nội dung:
    Subject: Special offer for {company}
    Body: Hello {name},
          We have a special offer for you...
          Best regards, Your Company
    """
    
    # AI thực hiện
    # - Mở Gmail
    # - Click New
    # - Điền To: email
    # - Điền Subject
    # - Điền Body
    # - Click Send
    
    print(f"✓ Email sent to {email}")
    time.sleep(5)  # Tránh rate limit
```

**Chạy:**
```bash
python examples/mail_merge.py
```

---

### Ví Dụ 5: Tạo Report Tự Động

**Yêu cầu:**
```
Tạo báo cáo hàng tháng từ Google Analytics, lưu thành PDF
```

**Steps:**
```
1. Mở Google Analytics
2. Select thời gian: tháng này
3. Export dữ liệu → CSV
4. Mở Excel, import CSV
5. Tạo biểu đồ
6. Save as PDF
```

---

### Ví Dụ 6: Chuyển Đổi Format Tài Liệu

**Yêu cầu:**
```
Chuyển 50 file .doc thành .pdf
```

**Command:**
```bash
python main.py

# Input:
# > Chuyển đổi tất cả file .doc trong folder "documents" thành .pdf

# Steps:
# 1. Liệt kê file .doc
# 2. Mở mỗi file trong Word
# 3. Save As → PDF
# 4. Lặp cho file tiếp theo
```

---

## 🧪 Nhóm 3: Testing & QA

### Ví Dụ 7: Test Login

**Yêu cầu:**
```
Test login form trên localhost:3000 với các case:
1. Valid login (success)
2. Wrong password (error)
3. Non-existent user (error)
```

**File: `examples/test_login.py`**

```python
from brain import Brain
from vision import Vision
from actions import Actions
import time

def test_login_case(username, password, expect_result):
    """Test một login case"""
    
    vision = Vision()
    actions = Actions()
    brain = Brain()
    
    # 1. Mở trang login
    actions.open_url("http://localhost:3000/login")
    time.sleep(2)
    
    # 2. Chụp ảnh ban đầu
    img = vision.capture_screen()
    
    # 3. Yêu cầu AI điền form
    prompt = f"""
    Điền username: {username}
    Điền password: {password}
    Nhấn login button
    """
    
    # 4. AI thực hiện
    # (tự động find fields, type, click)
    
    # 5. Chụp kết quả
    time.sleep(1)
    result_img = vision.capture_screen()
    
    # 6. Kiểm tra kết quả
    result_prompt = f"""
    Kiểm tra login có thành công không?
    Expected: {expect_result}
    Chụp ảnh hiện tại có hiển thị gì?
    """
    
    analysis = brain.analyze_and_decide(result_img, result_prompt)
    
    print(f"✓ Test {username}: {analysis['thought']}")

# Chạy test cases
test_login_case("validuser@test.com", "CorrectPass123", "success")
test_login_case("validuser@test.com", "WrongPassword", "error_message")
test_login_case("nonexistent@test.com", "AnyPassword", "error_message")
```

**Chạy:**
```bash
python examples/test_login.py

# Output:
# ✓ Test validuser@test.com: Login successful, redirected to dashboard
# ✓ Test validuser@test.com: Error message shown: "Invalid credentials"
# ✓ Test nonexistent@test.com: Error message shown: "User not found"
```

---

### Ví Dụ 8: Test Responsive Design

**Yêu cầu:**
```
Test website hoạt động tốt trên 3 kích thước màn hình:
- Desktop (1920x1080)
- Tablet (768x1024)
- Mobile (375x667)
```

**Script:**
```bash
python main.py

# Input:
# > Test responsive design của https://mywebsite.com trên desktop, tablet, mobile

# Steps:
# 1. Set resolution → 1920x1080 (desktop)
#    - Chụp ảnh trang chủ
#    - Check layout ok
# 2. Set resolution → 768x1024 (tablet)
#    - Chụp ảnh
#    - Check responsive
# 3. Set resolution → 375x667 (mobile)
#    - Chụp ảnh
#    - Check mobile view
# 4. Compare 3 ảnh
# 5. Report: "Layout responsive ✓" hoặc "Issues found: ..."
```

---

### Ví Dụ 9: Automation Test Suite

**Yêu cầu:**
```
Chạy test automation suite hoàn chỉnh
```

**File: `examples/test_suite.py`**

```python
"""
Chạy 10 test cases liên tiếp, report kết quả
"""

import sys
sys.path.insert(0, '..')

from brain import Brain
from vision import Vision
from actions import Actions
import time
import json

test_results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "tests": []
}

def run_test(name, commands):
    """Chạy một test"""
    global test_results
    
    print(f"\n📋 Running test: {name}")
    test_results["total"] += 1
    
    vision = Vision()
    actions = Actions()
    brain = Brain()
    
    try:
        for cmd in commands:
            if cmd['type'] == 'navigate':
                actions.open_url(cmd['url'])
            elif cmd['type'] == 'click':
                img = vision.capture_screen()
                # AI finds and clicks
            elif cmd['type'] == 'type':
                actions.type_text(cmd['text'])
            elif cmd['type'] == 'screenshot':
                vision.capture_screen()
            
            time.sleep(1)
        
        test_results["passed"] += 1
        test_results["tests"].append({
            "name": name,
            "status": "PASSED"
        })
        print(f"✓ PASSED: {name}")
        
    except Exception as e:
        test_results["failed"] += 1
        test_results["tests"].append({
            "name": name,
            "status": "FAILED",
            "error": str(e)
        })
        print(f"✗ FAILED: {name} - {e}")

# Test cases
run_test("Test 1: Navigate to homepage", [
    {"type": "navigate", "url": "http://localhost:3000"},
    {"type": "screenshot"}
])

run_test("Test 2: Search functionality", [
    {"type": "navigate", "url": "http://localhost:3000"},
    {"type": "screenshot"},
    # AI finds search box and types
])

# ... more tests ...

# Report
print("\n" + "="*50)
print("📊 TEST REPORT")
print("="*50)
print(f"Total: {test_results['total']}")
print(f"Passed: {test_results['passed']} ✓")
print(f"Failed: {test_results['failed']} ✗")
print(f"Pass rate: {(test_results['passed']/test_results['total']*100):.1f}%")
print("="*50)

# Save report
with open("test_report.json", "w") as f:
    json.dump(test_results, f, indent=2)
```

---

## 📱 Nhóm 4: Social Media Automation

### Ví Dụ 10: Post Facebook

**Yêu cầu:**
```
Đăng bài viết lên Facebook profile
```

**Command:**
```bash
python main.py

# Input:
# > Đăng bài viết lên Facebook: "Chào cả nhà! 👋 #hello"

# Steps:
# 1. Mở Facebook
# 2. Click "What's on your mind?"
# 3. Gõ bài viết
# 4. Add emoji
# 5. Click "Post"
# ✓ Posted!
```

---

### Ví Dụ 11: Schedule Tweets

**Yêu cầu:**
```
Đăng 5 tweet từng cái 1 giờ
```

**File: `examples/schedule_tweets.py`**

```python
import time
from actions import Actions

tweets = [
    "Just launched our new AI product! 🚀 #AI",
    "Big thanks to our amazing team 🙌",
    "Check out our blog post on AI agents 📚",
    "Join our community! Link in bio 🔗",
    "Thanks for the support! See you next time 👋"
]

actions = Actions()

for i, tweet in enumerate(tweets):
    print(f"📤 Posting tweet {i+1}/{len(tweets)}: {tweet}")
    
    actions.open_url("https://twitter.com/compose")
    actions.type_text(tweet)
    actions.hotkey("ctrl", "enter")  # Post
    
    time.sleep(3600)  # Chờ 1 giờ
```

---

### Ví Dụ 12: Bulk Follow Instagram

**Yêu cầu:**
```
Theo dõi 100 người dùng Instagram từ danh sách
```

**File: `examples/bulk_follow.py`**

```python
from brain import Brain
from actions import Actions
import time

users_to_follow = [
    "username1",
    "username2",
    # ... 100 users
]

for user in users_to_follow:
    actions = Actions()
    
    # 1. Vào profile
    actions.open_url(f"https://instagram.com/{user}")
    time.sleep(2)
    
    # 2. Click follow
    # (AI sẽ find & click follow button)
    
    print(f"✓ Followed {user}")
    time.sleep(3)  # Tránh rate limit
```

---

## 🖥️ Nhóm 5: System Administration

### Ví Dụ 13: Backup Files

**Yêu cầu:**
```
Backup tất cả file từ "Documents" sang external drive
```

**Command:**
```bash
python main.py

# Input:
# > Backup tất cả file trong Documents sang USB drive

# Steps:
# 1. Mở File Explorer
# 2. Navigate đến Documents
# 3. Select All (Ctrl+A)
# 4. Copy (Ctrl+C)
# 5. Navigate đến USB
# 6. Paste (Ctrl+V)
# 7. Chờ hoàn thành
# ✓ Backup complete!
```

---

### Ví Dụ 14: Monitor Process

**Yêu cầu:**
```
Kiểm tra CPU/Memory usage, cảnh báo nếu quá cao
```

**File: `examples/monitor.py`**

```python
import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    
    print(f"CPU: {cpu_percent}% | Memory: {memory_percent}%")
    
    if cpu_percent > 80:
        print("⚠️  WARNING: CPU usage high!")
        # Có thể trigger agent để close apps
    
    if memory_percent > 90:
        print("⚠️  WARNING: Memory usage critical!")
    
    time.sleep(60)  # Check mỗi phút
```

---

### Ví Dụ 15: Batch Rename Files

**Yêu cầu:**
```
Rename 50 file từ "IMG_001.jpg" thành "Photo_001.jpg"
```

**Command:**
```bash
python main.py

# Input:
# > Rename tất cả file IMG_*.jpg trong folder Downloads 
# > thành Photo_*.jpg

# Steps:
# 1. Mở File Explorer
# 2. Navigate đến Downloads
# 3. Select tất cả IMG file
# 4. Right-click → Rename
# 5. Đổi pattern: IMG → Photo
# ✓ Renamed 50 files
```

---

## 📊 Nhóm 6: Data Processing

### Ví Dụ 16: CSV Import/Export

**Yêu cầu:**
```
Import CSV file, process dữ liệu, export kết quả
```

**File: `examples/process_csv.py`**

```python
import pandas as pd

# Step 1: Import
df = pd.read_csv("sales_data.csv")
print(f"Loaded {len(df)} rows")

# Step 2: Process
df['Total'] = df['Price'] * df['Quantity']
df['Total_VND'] = df['Total'] * 24000  # Convert to VND

# Step 3: Export
df.to_csv("sales_processed.csv", index=False)
df.to_excel("sales_processed.xlsx", index=False)

print("✓ Done!")
```

---

### Ví Dụ 17: Format Data

**Yêu cầu:**
```
Chuẩn hóa dữ liệu: điều chỉnh định dạng ngày, loại bỏ whitespace, v.v.
```

---

### Ví Dụ 18: Merge Spreadsheets

**Yêu cầu:**
```
Gộp 5 file Excel thành 1
```

---

## 🎨 Nhóm 7: Creative & Content

### Ví Dụ 19: Batch Image Resize

**Yêu cầu:**
```
Resize 100 ảnh từ thư mục khác thành 50% kích thước
```

**File: `examples/batch_resize.py`**

```python
from PIL import Image
import os

image_dir = "images/"
output_dir = "images_resized/"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(os.path.join(image_dir, filename))
        
        # Resize 50%
        new_size = (img.width // 2, img.height // 2)
        resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Save
        resized.save(os.path.join(output_dir, filename))
        print(f"✓ Resized {filename}")
```

---

### Ví Dụ 20: Video Thumbnail Extraction

**Yêu cầu:**
```
Extract thumbnail từ 20 video files
```

---

## 🚀 Cách Chạy Các Ví Dụ

### Cách 1: Interactive Mode

```bash
python main.py
# Sau đó, gõ yêu cầu của bạn
```

### Cách 2: Script Mode

```bash
python examples/mail_merge.py
python examples/test_login.py
python examples/schedule_tweets.py
```

### Cách 3: Custom Script

```bash
# Tạo file mới
cat > my_task.py << 'EOF'
from brain import Brain
from actions import Actions

# Your custom code here
EOF

python my_task.py
```

---

## 💡 Mẹo & Tricks

1. **Combine tasks**: Thực hiện nhiều task liên tiếp
2. **Parallel execution**: Chạy multiple agents (với cảnh báo!)
3. **Custom prompts**: Tùy chỉnh system prompt trong brain.py
4. **Data export**: Luôn export kết quả thành CSV/JSON để dễ xử lý
5. **Schedule tasks**: Dùng cron (Linux) hoặc Task Scheduler (Windows)

---

## 🎓 Learn More

- Đọc [README.md](./README.md) để hiểu overall
- Đọc [config.py](./config.py) để tìm tùy chọn cấu hình
- Đọc source code: [brain.py](./brain.py), [vision.py](./vision.py), [actions.py](./actions.py)
- Xem logs để debug

---

**Happy Automating! 🎉**
