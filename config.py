"""
Cấu hình toàn cục cho AI Agent Computer Use.
Chỉnh sửa file này để tùy biến hành vi của Agent.
"""
import pyautogui

# ============================================================
# SCREEN
# ============================================================
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# ============================================================
# SAFETY - An toàn
# ============================================================
pyautogui.FAILSAFE = True          # Di chuột vào góc trên trái để dừng khẩn cấp
pyautogui.PAUSE = 0.3              # Delay nhỏ giữa mỗi lệnh pyautogui
MAX_STEPS = 30                     # Số bước tối đa mỗi task
STEP_DELAY = 12.0                  # Chờ 12s giữa mỗi bước ĐỂ TRÁNH RATE LIMIT 5 req/min của AI Free
EMERGENCY_STOP_CORNER_SIZE = 5     # Pixel ở góc màn hình để trigger dừng khẩn cấp
SHOW_OVERLAY = False               # Hiển thị viền xanh và nút Stop khi chạy (Có thể tắt nếu AI hay click nhầm)

# ============================================================
# MOUSE - Chuột
# ============================================================
MOUSE_MOVE_DURATION = 0.4          # Thời gian di chuyển chuột (giây)
MOUSE_CLICK_DELAY = 0.1            # Delay sau khi click
HUMAN_LIKE_MOUSE = True            # Di chuột theo đường cong tự nhiên

# ============================================================
# KEYBOARD - Bàn phím  
# ============================================================
TYPE_INTERVAL = 0.04               # Khoảng cách giữa mỗi phím khi gõ chữ
TYPE_DELAY_AFTER = 0.3             # Delay sau khi gõ xong

# ============================================================
# VISION - Thị giác
# ============================================================
SCREENSHOT_DIR = "screenshots"     # Thư mục lưu ảnh chụp màn hình
GRID_ENABLED = True                # Vẽ Grid lưới tọa độ lên ảnh
GRID_ROWS = 10                     # Số hàng grid
GRID_COLS = 16                     # Số cột grid  
GRID_COLOR = (0, 255, 0)           # Màu grid (BGR - xanh lá)
GRID_ALPHA = 0.15                  # Độ trong suốt grid
GRID_LABEL_SIZE = 0.4              # Cỡ chữ label grid

# ============================================================
# AI BRAIN - Bộ não
# ============================================================
# Danh sách provider ưu tiên (theo thứ tự thử)
# Chỉ dùng các provider KHÔNG cần API key, KHÔNG tự mở web
PREFERRED_PROVIDERS = [
    "PollinationsAI",     # CONFIRMED WORKING - Free, no auth
    "BlackboxPro",        # Free, no auth
    "DeepInfra",          # Free tier available
    "HuggingFace",        # Free, no auth
    "HuggingChat",        # Free, no auth
    "FenayAI",            # Free, no auth
    "Yqcloud",            # Free, no auth
    "ItalyGPT",           # Free, no auth
    "TeachAnything",      # Free, no auth
]

# Retry config
MAX_PROVIDER_RETRIES = 2           # Số lần thử lại mỗi provider (giảm để nhanh hơn)
BRAIN_TIMEOUT = 30                 # Timeout cho mỗi request AI (giây)

# ============================================================
# LOGGING
# ============================================================
LOG_FILE = "agent.log"
VERBOSE = True                     # In chi tiết ra terminal
SAVE_SCREENSHOTS = True            # Lưu ảnh mỗi bước

# ============================================================
# GRID SYSTEM - Hệ thống lưới
# ============================================================
# Chuyển đổi grid label (ví dụ "B3") thành tọa độ pixel
def grid_to_pixel(col_letter: str, row_number: int) -> tuple[int, int]:
    """Chuyển grid label như 'B3' thành tọa độ pixel (x, y) ở tâm ô."""
    col_index = ord(col_letter.upper()) - ord('A')
    row_index = row_number - 1
    
    cell_width = SCREEN_WIDTH / GRID_COLS
    cell_height = SCREEN_HEIGHT / GRID_ROWS
    
    x = int(col_index * cell_width + cell_width / 2)
    y = int(row_index * cell_height + cell_height / 2)
    
    return (x, y)
