"""
🔍 VISION MODULE - Đôi mắt của AI Agent
==========================================
Module này chịu trách nhiệm:
1. Chụp ảnh màn hình cực nhanh (dùng mss thay vì pyautogui - nhanh hơn 10x)
2. Vẽ Grid System lên ảnh (giúp AI nhận diện tọa độ chính xác hơn)
3. Thu thập thông tin hệ thống (cửa sổ đang mở, tiêu đề, v.v.)
"""

import os
import time
import base64
from io import BytesIO
from datetime import datetime

import mss
import mss.tools
from PIL import Image, ImageDraw, ImageFont
import pyautogui
import psutil

import config


class Vision:
    """Đôi mắt của AI - chụp và xử lý ảnh màn hình."""
    
    def __init__(self):
        self.screenshot_count = 0
        
        # Tạo thư mục screenshots
        os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
    
    # ─── CHỤP MÀN HÌNH ──────────────────────────────────────────
    
    def capture_screen(self, save: bool = True) -> Image.Image:
        """
        Chụp ảnh toàn bộ màn hình.
        Dùng mss thay vì pyautogui.screenshot() vì nhanh hơn ~10 lần.
        """
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Monitor chính
            raw = sct.grab(monitor)
            img = Image.frombytes("RGB", raw.size, raw.rgb)
        
        self.screenshot_count += 1
        
        if save and config.SAVE_SCREENSHOTS:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(
                config.SCREENSHOT_DIR, 
                f"step_{self.screenshot_count:03d}_{timestamp}.png"
            )
            img.save(path, optimize=True)
        
        return img
    
    # ─── GRID SYSTEM ─────────────────────────────────────────────
    
    def draw_grid(self, img: Image.Image) -> Image.Image:
        """
        Vẽ Grid System lên ảnh màn hình.
        Grid giúp AI xác định tọa độ chính xác hơn rất nhiều so với 
        việc đoán pixel trực tiếp.
        
        Mỗi ô được đánh nhãn: A1, A2, ... P10
        (16 cột x 10 hàng = 160 ô bao phủ toàn màn hình)
        """
        if not config.GRID_ENABLED:
            return img
        
        # Tạo overlay trong suốt
        overlay = img.copy()
        draw = ImageDraw.Draw(overlay)
        
        w, h = img.size
        cell_w = w / config.GRID_COLS
        cell_h = h / config.GRID_ROWS
        
        # Vẽ các đường kẻ dọc
        for i in range(config.GRID_COLS + 1):
            x = int(i * cell_w)
            draw.line([(x, 0), (x, h)], fill=(0, 255, 0), width=1)
        
        # Vẽ các đường kẻ ngang
        for j in range(config.GRID_ROWS + 1):
            y = int(j * cell_h)
            draw.line([(0, y), (w, y)], fill=(0, 255, 0), width=1)
        
        # Vẽ nhãn cho mỗi ô
        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except (IOError, OSError):
            font = ImageFont.load_default()
        
        for col in range(config.GRID_COLS):
            for row in range(config.GRID_ROWS):
                label = f"{chr(65 + col)}{row + 1}"
                x = int(col * cell_w + 4)
                y = int(row * cell_h + 2)
                
                # Nền đen nhỏ cho dễ đọc
                bbox = font.getbbox(label)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                draw.rectangle(
                    [x - 1, y - 1, x + text_w + 3, y + text_h + 3],
                    fill=(0, 0, 0, 180)
                )
                draw.text((x, y), label, fill=(0, 255, 0), font=font)
        
        # Blend overlay với ảnh gốc
        return Image.blend(img, overlay, config.GRID_ALPHA)
    
    # ─── CHUẨN BỊ ẢNH GỬI AI ────────────────────────────────────
    
    def get_screenshot_for_ai(self) -> Image.Image:
        """
        Chụp màn hình + vẽ grid + resize cho phù hợp gửi AI.
        Trả về ảnh PIL Image sẵn sàng gửi cho brain.
        """
        img = self.capture_screen()
        img_with_grid = self.draw_grid(img)
        
        # Resize xuống để giảm token khi gửi AI (giữ tỷ lệ)
        max_width = 1280
        if img_with_grid.width > max_width:
            ratio = max_width / img_with_grid.width
            new_h = int(img_with_grid.height * ratio)
            img_with_grid = img_with_grid.resize(
                (max_width, new_h), Image.LANCZOS
            )
        
        return img_with_grid
    
    def image_to_base64(self, img: Image.Image) -> str:
        """Chuyển ảnh PIL thành base64 string để gửi qua API."""
        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=75)
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    # ─── THU THẬP THÔNG TIN HỆ THỐNG ─────────────────────────────
    
    def get_system_context(self) -> str:
        """
        Thu thập thông tin hệ thống hiện tại:
        - Vị trí chuột
        - Các cửa sổ đang mở
        - CPU/RAM usage
        
        Dùng khi AI không nhìn được ảnh (fallback text-only).
        """
        info_parts = []
        
        # Vị trí chuột hiện tại
        mouse_x, mouse_y = pyautogui.position()
        info_parts.append(f"🖱️ Chuột tại: ({mouse_x}, {mouse_y})")
        
        # Kích thước màn hình
        info_parts.append(f"🖥️ Màn hình: {config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}")
        
        # Danh sách cửa sổ đang mở (Windows only)
        try:
            windows = pyautogui.getAllWindows()
            visible_windows = [
                w.title for w in windows 
                if w.title and w.isActive is not None
            ]
            if visible_windows:
                info_parts.append("📋 Cửa sổ đang mở:")
                for title in visible_windows[:10]:  # Max 10
                    info_parts.append(f"   - {title}")
        except Exception:
            pass
        
        # Active window
        try:
            active = pyautogui.getActiveWindow()
            if active and active.title:
                info_parts.append(f"🎯 Cửa sổ đang active: '{active.title}'")
                info_parts.append(f"   Vị trí: ({active.left}, {active.top})")
                info_parts.append(f"   Kích thước: {active.width}x{active.height}")
        except Exception:
            pass
        
        # System resources
        try:
            cpu = psutil.cpu_percent(interval=0.1)
            ram = psutil.virtual_memory().percent
            info_parts.append(f"⚡ CPU: {cpu}% | RAM: {ram}%")
        except Exception:
            pass
        
        return "\n".join(info_parts)
    
    def get_active_window_title(self) -> str:
        """Lấy tiêu đề cửa sổ đang active."""
        try:
            active = pyautogui.getActiveWindow()
            if active:
                return active.title or "Unknown"
        except Exception:
            pass
        return "Unknown"


# Singleton instance
vision = Vision()
