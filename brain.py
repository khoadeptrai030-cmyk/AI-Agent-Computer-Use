"""
BRAIN MODULE - Bo nao cua AI Agent
========================================
Module nay chiu trach nhiem:
1. Ket noi voi AI mien phi qua g4f (GPT4Free)
2. Gui anh man hinh + prompt cho AI phan tich
3. Nhan va parse JSON response
4. Tu dong fallback giua cac provider
5. Quan ly lich su hoi thoai (memory)

KHONG yeu cau API key. KHONG tu mo web. KHONG gioi han luot nhan.
"""

import os
import sys
import json
import re
import time
import traceback
from typing import Optional

# Fix Windows console encoding
if sys.platform == "win32":
    os.system("")
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import g4f
from g4f.client import Client

import config
from vision import vision


class Brain:
    """Bộ não AI - suy nghĩ và ra quyết định."""
    
    def __init__(self):
        self.client = Client()
        self.history = []
        self.step_count = 0
        self.working_provider = None  # Cache provider hoạt động
        
        # Tìm providers khả dụng
        self.providers = self._discover_providers()
        
        # System prompt - "Linh hồn" của Agent
        self.system_prompt = self._build_system_prompt()
    
    # ─── TÌM PROVIDER ────────────────────────────────────────────
    
    def _discover_providers(self) -> list:
        """
        Tự động tìm và kiểm tra providers khả dụng.
        Chỉ dùng provider không cần auth, không mở browser.
        """
        available = []
        
        for name in config.PREFERRED_PROVIDERS:
            if hasattr(g4f.Provider, name):
                provider = getattr(g4f.Provider, name)
                available.append(provider)
                if config.VERBOSE:
                    print(f"  [OK] Provider kha dung: {name}")
            else:
                if config.VERBOSE:
                    print(f"  [--] Provider khong tim thay: {name}")
        
        if not available:
            print("  [WARN] Khong tim thay provider nao! Se dung auto-detect.")
        
        return available
    
    # ─── SYSTEM PROMPT ────────────────────────────────────────────
    
    def _build_system_prompt(self) -> str:
        """Xây dựng system prompt chi tiết cho AI."""
        return f"""Bạn là một AI Agent tự chủ điều khiển máy tính Windows.
Bạn PHẢI phân tích ảnh chụp màn hình và thực hiện hành động để hoàn thành nhiệm vụ.

═══════════════════════════════════════════════════════
📏 THÔNG TIN MÀN HÌNH
═══════════════════════════════════════════════════════
- Độ phân giải: {config.SCREEN_WIDTH} x {config.SCREEN_HEIGHT}
- Grid System: {config.GRID_COLS} cột (A-P) x {config.GRID_ROWS} hàng (1-10)
- Mỗi ô grid: {config.SCREEN_WIDTH // config.GRID_COLS}x{config.SCREEN_HEIGHT // config.GRID_ROWS} pixels
- Ô A1 = góc trên trái, P10 = góc dưới phải

═══════════════════════════════════════════════════════
🎯 QUY TẮC XÁC ĐỊNH TỌA ĐỘ
═══════════════════════════════════════════════════════
1. Nhìn vào nhãn Grid trên ảnh (A1, B2, C5, ...)
2. Xác định phần tử UI nằm ở ô Grid nào
3. Ước tính tọa độ pixel chính xác trong ô đó
4. Tọa độ (0,0) = góc trên trái; ({config.SCREEN_WIDTH},{config.SCREEN_HEIGHT}) = góc dưới phải

═══════════════════════════════════════════════════════
📋 DANH SÁCH HÀNH ĐỘNG
═══════════════════════════════════════════════════════
Bạn CHỈ ĐƯỢC phản hồi bằng JSON với một trong các action sau:

1. Click chuột:
   {{"action_type": "click", "x": 500, "y": 300}}

2. Double click:
   {{"action_type": "double_click", "x": 500, "y": 300}}

3. Right click:
   {{"action_type": "right_click", "x": 500, "y": 300}}

4. Gõ văn bản:
   {{"action_type": "type", "text": "Hello World", "press_enter": true}}

5. Nhấn phím:
   {{"action_type": "press_key", "key": "enter"}}

6. Tổ hợp phím:
   {{"action_type": "hotkey", "keys": ["ctrl", "c"]}}

7. Scroll:
   {{"action_type": "scroll", "amount": -3, "x": 960, "y": 540}}
   (amount > 0 = lên, < 0 = xuống)

8. Kéo thả:
   {{"action_type": "drag", "start_x": 100, "start_y": 200, "end_x": 400, "end_y": 500}}

9. Mở ứng dụng (tìm trong Start Menu):
   {{"action_type": "open_app", "app_name": "Notepad"}}

10. Mở URL:
    {{"action_type": "open_url", "url": "https://google.com"}}

11. Đóng cửa sổ:
    {{"action_type": "close_window"}}

12. Chuyển cửa sổ:
    {{"action_type": "switch_window"}}

13. Chờ (khi cần đợi tải):
    {{"action_type": "wait", "seconds": 2}}

14. Hoàn thành:
    {{"action_type": "done", "summary": "Đã hoàn thành: mở Notepad và gõ Hello"}}

═══════════════════════════════════════════════════════
📝 FORMAT PHẢN HỒI (BẮT BUỘC)
═══════════════════════════════════════════════════════
```json
{{
    "thought": "Mô tả suy nghĩ: Tôi thấy gì trên màn hình, cần làm gì tiếp",
    "action_type": "...",
    "...các tham số tương ứng..."
}}
```

═══════════════════════════════════════════════════════
⚠️ QUY TẮC QUAN TRỌNG
═══════════════════════════════════════════════════════
1. LUÔN phân tích ảnh trước, KHÔNG đoán mò
2. Nếu hành động trước thất bại → thử cách khác (ĐỪNG lặp lại hành động cũ)
3. Nếu thấy popup/dialog → xử lý nó trước (đóng hoặc click OK)
4. Nếu cần chờ tải → dùng action "wait"
5. Khi hoàn thành → PHẢI dùng action "done" với summary
6. CHỈ trả về JSON thuần. KHÔNG kèm text giải thích bên ngoài.
"""
    
    # ─── GỌI AI ──────────────────────────────────────────────────
    
    def think(self, task: str, screenshot=None, system_context: str = None) -> Optional[dict]:
        """
        Gửi thông tin cho AI và nhận quyết định hành động.
        
        Args:
            task: Nhiệm vụ cần thực hiện
            screenshot: PIL Image của màn hình (hoặc None)
            system_context: Thông tin hệ thống dạng text (fallback)
        
        Returns:
            dict chứa action, hoặc None nếu thất bại
        """
        self.step_count += 1
        
        # Xây dựng message
        messages = self._build_messages(task, screenshot, system_context)
        
        # Thử gọi AI với các provider
        response_text = self._call_ai(messages, has_image=screenshot is not None)
        
        if response_text is None:
            print("  [FAIL] Tat ca providers deu that bai!")
            return None
        
        # Parse JSON response
        action = self._parse_response(response_text)
        
        if action:
            # Lưu vào history
            self.history.append({
                "step": self.step_count,
                "thought": action.get("thought", ""),
                "action": action.get("action_type", ""),
            })
        
        return action
    
    def _build_messages(self, task, screenshot, system_context):
        """Xây dựng danh sách messages cho AI."""
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        # Thêm lịch sử gần nhất (max 5 bước)
        if self.history:
            history_text = "📜 Lịch sử các bước đã thực hiện:\n"
            for h in self.history[-5:]:
                history_text += f"  Bước {h['step']}: [{h['action']}] {h['thought']}\n"
            messages.append({"role": "user", "content": history_text})
            messages.append({"role": "assistant", "content": "Đã ghi nhận lịch sử. Tôi sẽ phân tích màn hình hiện tại."})
        
        # Message chính
        user_content = f"🎯 NHIỆM VỤ: {task}\n\n📍 Bước hiện tại: {self.step_count}\n"
        
        if system_context:
            user_content += f"\n📊 THÔNG TIN HỆ THỐNG:\n{system_context}\n"
        
        user_content += "\nHãy phân tích màn hình và cho tôi hành động tiếp theo (JSON)."
        
        if screenshot:
            # Gửi kèm ảnh
            img_b64 = vision.image_to_base64(screenshot)
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": user_content},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}
                    }
                ]
            })
        else:
            messages.append({"role": "user", "content": user_content})
        
        return messages
    
    def _call_ai(self, messages: list, has_image: bool = False) -> Optional[str]:
        """
        Gọi AI với cơ chế fallback:
        1. Tạo sẵn 2 payload: 1 có ảnh, 1 chỉ có text
        2. Nếu provider hỗ trợ vision (PollinationsAI) -> gửi ảnh
        3. Nếu provider không hỗ trợ -> gửi text ngay lập tức để tránh bị treo
        """
        VISION_PROVIDERS = ["PollinationsAI", "BlackboxPro"]
        
        # Chuẩn bị payload text-only
        text_messages = []
        for msg in messages:
            if isinstance(msg.get("content"), list):
                text_parts = [p["text"] for p in msg["content"] if p.get("type") == "text"]
                text_messages.append({
                    "role": msg["role"],
                    "content": "\n".join(text_parts) + "\n[Ảnh không gửi được, hãy dựa vào thông tin hệ thống]"
                })
            else:
                text_messages.append(msg)
        
        # Phương án 1: Dùng provider đã cache (nhanh nhất)
        if self.working_provider:
            name = self.working_provider.__name__
            payload = messages if (has_image and name in VISION_PROVIDERS) else text_messages
            result = self._try_provider(self.working_provider, payload)
            if result:
                return result
            self.working_provider = None
        
        # Phương án 2: Thử từng provider
        for provider in self.providers:
            name = provider.__name__
            payload = messages if (has_image and name in VISION_PROVIDERS) else text_messages
            result = self._try_provider(provider, payload)
            if result:
                self.working_provider = provider  # Cache lại
                return result
        
        return None
    
    def _try_provider(self, provider, messages: list) -> Optional[str]:
        """Thử gọi một provider cụ thể."""
        name = provider.__name__ if provider else "Auto"
        
        for attempt in range(config.MAX_PROVIDER_RETRIES):
            try:
                if config.VERBOSE:
                    suffix = f" (lần {attempt+1})" if attempt > 0 else ""
                    print(f"  [BRAIN] Thu: {name}{suffix}...")
                
                kwargs = {
                    "messages": messages,
                }
                if provider:
                    kwargs["provider"] = provider
                    # Use the provider's own default model for best compatibility
                    default_model = getattr(provider, 'default_model', '') or ''
                    kwargs["model"] = default_model if default_model else "gpt-4o-mini"
                else:
                    kwargs["model"] = ""  # Let g4f auto-select
                
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(self.client.chat.completions.create, **kwargs)
                    try:
                        response = future.result(timeout=config.BRAIN_TIMEOUT)
                    except concurrent.futures.TimeoutError:
                        if config.VERBOSE:
                            print(f"  [TIMEOUT] {name} khong phan hoi sau {config.BRAIN_TIMEOUT}s (co the do up anh)")
                        break # Skip retry on timeout
                
                result = response.choices[0].message.content
                if result and len(result.strip()) > 5:
                    if config.VERBOSE:
                        print(f"  [OK] {name} phan hoi thanh cong!")
                    return result
                else:
                    if config.VERBOSE:
                        print(f"  [WARN] {name} tra ve rong")
                        
            except Exception as e:
                error_msg = str(e)[:100]
                if config.VERBOSE:
                    print(f"  [ERR] {name} loi: {error_msg}")
                
                # Không retry nếu lỗi auth/key hoặc rate limit
                lower_err = error_msg.lower()
                if any(kw in lower_err for kw in ["api_key", "cookie", "auth", "login", "rate limit", "request limit", "decode"]):
                    break
                
                time.sleep(0.5)
        
        return None
    
    # ─── PARSE RESPONSE ──────────────────────────────────────────
    
    def _parse_response(self, text: str) -> Optional[dict]:
        """
        Parse phản hồi JSON từ AI.
        Xử lý nhiều trường hợp: JSON thuần, markdown code block, 
        text lẫn JSON, v.v.
        """
        if not text:
            return None
        
        text = text.strip()
        
        # Thử 1: Parse trực tiếp
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
        
        # Thử 2: Trích xuất từ markdown code block
        code_block = re.search(r'```(?:json)?\s*\n?(.*?)\n?\s*```', text, re.DOTALL)
        if code_block:
            try:
                return json.loads(code_block.group(1).strip())
            except json.JSONDecodeError:
                pass
        
        # Thử 3: Tìm JSON object trong text
        json_match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Thử 4: Sửa JSON phổ biến (trailing comma, single quotes)
        cleaned = text
        cleaned = re.sub(r',\s*}', '}', cleaned)  # Trailing comma
        cleaned = re.sub(r',\s*]', ']', cleaned)
        cleaned = cleaned.replace("'", '"')         # Single quotes
        
        json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Thử 5: Trích xuất thủ công nếu có từ khóa action
        if "action_type" in text.lower() or "click" in text.lower():
            return self._extract_action_manually(text)
        
        print(f"  [WARN] Khong parse duoc JSON. Raw: {text[:200]}...")
        return None
    
    def _extract_action_manually(self, text: str) -> Optional[dict]:
        """
        Cố gắng trích xuất action từ text không phải JSON.
        Dùng regex để tìm các thành phần.
        """
        result = {"thought": "Extracted from non-JSON response"}
        
        # Tìm action_type
        action_match = re.search(
            r'action_type["\s:]+["\']?(click|double_click|type|press_key|hotkey|scroll|open_app|open_url|wait|done|right_click|drag|close_window|switch_window|open_start|open_run|minimize_all)["\']?',
            text, re.IGNORECASE
        )
        if action_match:
            result["action_type"] = action_match.group(1).lower()
        else:
            return None
        
        # Tìm tọa độ x, y
        x_match = re.search(r'"x"\s*:\s*(\d+)', text)
        y_match = re.search(r'"y"\s*:\s*(\d+)', text)
        if x_match:
            result["x"] = int(x_match.group(1))
        if y_match:
            result["y"] = int(y_match.group(1))
        
        # Tìm text
        text_match = re.search(r'"text"\s*:\s*"([^"]*)"', text)
        if text_match:
            result["text"] = text_match.group(1)
        
        # Tìm key
        key_match = re.search(r'"key"\s*:\s*"([^"]*)"', text)
        if key_match:
            result["key"] = key_match.group(1)
        
        return result
    
    # ─── RESET ────────────────────────────────────────────────────
    
    def reset(self):
        """Reset bộ não cho nhiệm vụ mới."""
        self.history = []
        self.step_count = 0
        print("  [BRAIN] Bo nao da reset.")


# Singleton instance
brain = Brain()