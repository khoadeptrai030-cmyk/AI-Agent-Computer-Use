"""
🖐️ ACTIONS MODULE - Đôi tay của AI Agent
==========================================
Module này chịu trách nhiệm:
1. Di chuyển chuột (mượt mà, giống người thật)
2. Click chuột (click, double click, right click)
3. Gõ bàn phím (Unicode support cho tiếng Việt)
4. Nhấn phím tắt (Ctrl+C, Alt+Tab, v.v.)
5. Scroll, drag & drop
6. Mở ứng dụng, file, URL
"""

import time
import subprocess
import math
import random

import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController

import config


class Actions:
    """Đôi tay của AI - thực hiện các thao tác trên máy tính."""
    
    def __init__(self):
        self.keyboard = KeyboardController()
        self.last_action = None
        self.action_count = 0
    
    # ─── CHUỘT ────────────────────────────────────────────────────
    
    def move_mouse(self, x: int, y: int):
        """Di chuyển chuột đến tọa độ (x, y) một cách mượt mà."""
        # Giới hạn trong màn hình
        x = max(0, min(x, config.SCREEN_WIDTH - 1))
        y = max(0, min(y, config.SCREEN_HEIGHT - 1))
        
        if config.HUMAN_LIKE_MOUSE:
            # Thêm offset nhỏ ngẫu nhiên (giống người thật)
            x += random.randint(-2, 2)
            y += random.randint(-2, 2)
            x = max(0, min(x, config.SCREEN_WIDTH - 1))
            y = max(0, min(y, config.SCREEN_HEIGHT - 1))
        
        pyautogui.moveTo(
            x, y, 
            duration=config.MOUSE_MOVE_DURATION,
            tween=pyautogui.easeInOutQuad
        )
    
    def click(self, x: int, y: int, button: str = "left"):
        """Click chuột tại vị trí (x, y)."""
        self.move_mouse(x, y)
        time.sleep(0.05)
        pyautogui.click(x, y, button=button)
        time.sleep(config.MOUSE_CLICK_DELAY)
        
        self.last_action = f"click({x}, {y}, {button})"
        self.action_count += 1
        return f"✅ Đã click {button} tại ({x}, {y})"
    
    def double_click(self, x: int, y: int):
        """Double click tại vị trí (x, y)."""
        self.move_mouse(x, y)
        time.sleep(0.05)
        pyautogui.doubleClick(x, y)
        time.sleep(config.MOUSE_CLICK_DELAY)
        
        self.last_action = f"double_click({x}, {y})"
        self.action_count += 1
        return f"✅ Đã double click tại ({x}, {y})"
    
    def right_click(self, x: int, y: int):
        """Right click tại vị trí (x, y)."""
        self.move_mouse(x, y)
        time.sleep(0.05)
        pyautogui.rightClick(x, y)
        time.sleep(config.MOUSE_CLICK_DELAY)
        
        self.last_action = f"right_click({x}, {y})"
        self.action_count += 1
        return f"✅ Đã right click tại ({x}, {y})"
    
    def scroll(self, amount: int, x: int = None, y: int = None):
        """
        Scroll chuột. 
        amount > 0: scroll lên, amount < 0: scroll xuống.
        """
        if x is not None and y is not None:
            self.move_mouse(x, y)
            time.sleep(0.05)
        
        pyautogui.scroll(amount)
        direction = "lên" if amount > 0 else "xuống"
        
        self.last_action = f"scroll({amount})"
        self.action_count += 1
        return f"✅ Đã scroll {direction} {abs(amount)} đơn vị"
    
    def drag(self, start_x: int, start_y: int, end_x: int, end_y: int):
        """Kéo thả từ (start_x, start_y) đến (end_x, end_y)."""
        self.move_mouse(start_x, start_y)
        time.sleep(0.1)
        pyautogui.drag(
            end_x - start_x, 
            end_y - start_y,
            duration=config.MOUSE_MOVE_DURATION * 2,
            tween=pyautogui.easeInOutQuad
        )
        
        self.last_action = f"drag({start_x},{start_y} -> {end_x},{end_y})"
        self.action_count += 1
        return f"✅ Đã kéo thả từ ({start_x},{start_y}) đến ({end_x},{end_y})"
    
    # ─── BÀN PHÍM ────────────────────────────────────────────────
    
    def type_text(self, text: str, press_enter: bool = False):
        """
        Gõ văn bản. Hỗ trợ Unicode (tiếng Việt).
        Dùng pynput thay vì pyautogui để hỗ trợ Unicode tốt hơn.
        """
        time.sleep(0.1)
        
        for char in text:
            try:
                self.keyboard.type(char)
                # Thêm độ trễ để giống người gõ thật
                delay = random.uniform(0.01, 0.05)
                time.sleep(delay)
            except Exception:
                # Fallback cho ký tự đặc biệt
                pyautogui.press(char)
                time.sleep(config.TYPE_INTERVAL)
        
        if press_enter:
            time.sleep(0.1)
            pyautogui.press("enter")
        
        time.sleep(config.TYPE_DELAY_AFTER)
        
        self.last_action = f"type('{text[:30]}...')" if len(text) > 30 else f"type('{text}')"
        self.action_count += 1
        return f"✅ Đã gõ: '{text}'"
    
    def press_key(self, key: str):
        """
        Nhấn một phím đơn.
        Hỗ trợ: enter, tab, escape, space, backspace, delete,
                 up, down, left, right, home, end, pageup, pagedown,
                 f1-f12, printscreen, capslock, numlock
        """
        key = key.lower().strip()
        pyautogui.press(key)
        time.sleep(0.1)
        
        self.last_action = f"press_key('{key}')"
        self.action_count += 1
        return f"✅ Đã nhấn phím: {key}"
    
    def hotkey(self, *keys):
        """
        Nhấn tổ hợp phím.
        Ví dụ: hotkey("ctrl", "c") → Ctrl+C
                hotkey("alt", "tab") → Alt+Tab
                hotkey("ctrl", "shift", "s") → Ctrl+Shift+S
        """
        pyautogui.hotkey(*keys)
        time.sleep(0.2)
        
        combo = "+".join(keys)
        self.last_action = f"hotkey({combo})"
        self.action_count += 1
        return f"✅ Đã nhấn tổ hợp: {combo}"
    
    # ─── TIỆN ÍCH ────────────────────────────────────────────────
    
    def open_start_menu(self):
        """Mở menu Start."""
        pyautogui.press("win")
        time.sleep(0.3)
        
        self.last_action = "open_start_menu()"
        self.action_count += 1
        return "✅ Đã mở Start Menu"
    
    def open_run_dialog(self):
        """Mở hộp thoại Run (Win+R)."""
        pyautogui.hotkey("win", "r")
        time.sleep(0.3)
        
        self.last_action = "open_run_dialog()"
        self.action_count += 1
        return "✅ Đã mở Run Dialog"
    
    def open_app(self, app_name: str):
        """
        Mở ứng dụng bằng cách tìm kiếm trong Start Menu.
        """
        pyautogui.press("win")
        time.sleep(0.8)  # Chờ Start menu lên
        
        self.type_text(app_name, press_enter=True)
        time.sleep(1.5)  # Chờ app mở lên
        
        self.last_action = f"open_app('{app_name}')"
        self.action_count += 1
        return f"✅ Đã mở ứng dụng: {app_name}"
    
    def open_url(self, url: str):
        """Mở URL trong trình duyệt mặc định."""
        try:
            subprocess.Popen(["cmd", "/c", "start", url], 
                           shell=True, 
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            time.sleep(2.0)
            
            self.last_action = f"open_url('{url}')"
            self.action_count += 1
            return f"✅ Đã mở URL: {url}"
        except Exception as e:
            return f"❌ Lỗi mở URL: {e}"
    
    def close_window(self):
        """Đóng cửa sổ hiện tại (Alt+F4)."""
        pyautogui.hotkey("alt", "F4")
        time.sleep(0.5)
        
        self.last_action = "close_window()"
        self.action_count += 1
        return "✅ Đã đóng cửa sổ"
    
    def switch_window(self):
        """Chuyển đổi cửa sổ (Alt+Tab)."""
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.5)
        
        self.last_action = "switch_window()"
        self.action_count += 1
        return "✅ Đã chuyển cửa sổ"
    
    def minimize_all(self):
        """Thu nhỏ tất cả cửa sổ (Win+D)."""
        pyautogui.hotkey("win", "d")
        time.sleep(0.5)
        
        self.last_action = "minimize_all()"
        self.action_count += 1
        return "✅ Đã thu nhỏ tất cả"
    
    def screenshot_to_clipboard(self):
        """Chụp ảnh màn hình vào clipboard (PrintScreen)."""
        pyautogui.press("printscreen")
        time.sleep(0.3)
        
        self.last_action = "screenshot_to_clipboard()"
        self.action_count += 1
        return "✅ Đã chụp ảnh vào clipboard"
    
    def wait(self, seconds: float = 2.0):
        """Chờ một khoảng thời gian."""
        time.sleep(seconds)
        
        self.last_action = f"wait({seconds}s)"
        self.action_count += 1
        return f"✅ Đã chờ {seconds} giây"
    
    # ─── THỰC THI TỪ JSON ─────────────────────────────────────────
    
    def execute(self, action_data: dict) -> tuple[bool, str]:
        """
        Thực thi một hành động từ dict JSON của AI.
        
        Returns:
            (is_done: bool, message: str)
            is_done = True nghĩa là nhiệm vụ hoàn thành.
        """
        action = action_data.get("action_type", "").lower().strip()
        
        try:
            if action == "click":
                x = int(action_data.get("x", 0))
                y = int(action_data.get("y", 0))
                msg = self.click(x, y)
                
            elif action == "double_click":
                x = int(action_data.get("x", 0))
                y = int(action_data.get("y", 0))
                msg = self.double_click(x, y)
                
            elif action == "right_click":
                x = int(action_data.get("x", 0))
                y = int(action_data.get("y", 0))
                msg = self.right_click(x, y)
                
            elif action == "type":
                text = action_data.get("text", "")
                press_enter = action_data.get("press_enter", False)
                msg = self.type_text(text, press_enter)
                
            elif action == "press_key":
                key = action_data.get("key", "")
                msg = self.press_key(key)
                
            elif action == "hotkey":
                keys = action_data.get("keys", [])
                if isinstance(keys, str):
                    keys = [k.strip() for k in keys.split("+")]
                msg = self.hotkey(*keys)
                
            elif action == "scroll":
                amount = int(action_data.get("amount", -3))
                x = action_data.get("x")
                y = action_data.get("y")
                if x is not None:
                    x = int(x)
                if y is not None:
                    y = int(y)
                msg = self.scroll(amount, x, y)
                
            elif action == "drag":
                msg = self.drag(
                    int(action_data.get("start_x", 0)),
                    int(action_data.get("start_y", 0)),
                    int(action_data.get("end_x", 0)),
                    int(action_data.get("end_y", 0))
                )
                
            elif action == "open_app":
                app = action_data.get("app_name", "")
                msg = self.open_app(app)
                
            elif action == "open_url":
                url = action_data.get("url", "")
                msg = self.open_url(url)
                
            elif action == "close_window":
                msg = self.close_window()
                
            elif action == "switch_window":
                msg = self.switch_window()
                
            elif action == "open_start":
                msg = self.open_start_menu()
                
            elif action == "open_run":
                msg = self.open_run_dialog()
                
            elif action == "minimize_all":
                msg = self.minimize_all()
                
            elif action == "wait":
                seconds = float(action_data.get("seconds", 2))
                msg = self.wait(seconds)
                
            elif action == "done":
                summary = action_data.get("summary", "Nhiệm vụ hoàn thành!")
                return (True, f"🎉 {summary}")
                
            else:
                msg = f"⚠️ Hành động không xác định: '{action}'"
            
            return (False, msg)
            
        except pyautogui.FailSafeException:
            return (True, "🛑 DỪNG KHẨN CẤP! Chuột đã di chuyển vào góc an toàn.")
        except Exception as e:
            return (False, f"❌ Lỗi thực hiện '{action}': {str(e)}")


# Singleton instance
actions = Actions()
