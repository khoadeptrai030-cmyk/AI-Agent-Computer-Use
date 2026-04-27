import tkinter as tk
import sys
import os
import urllib.request

def stop_agent(event=None):
    """Gọi API để stop server, sau đó đóng overlay."""
    try:
        req = urllib.request.Request("http://127.0.0.1:5000/api/stop", method="POST")
        urllib.request.urlopen(req, timeout=2)
    except Exception as e:
        pass
    root.destroy()
    os._exit(0)

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("AI Agent Overlay")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'gray')
root.config(bg='gray')

canvas = tk.Canvas(root, bg='gray', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Viền xanh cyan
border_thickness = 4
canvas.create_rectangle(0, 0, w, h, outline='#00f3ff', width=border_thickness*2)

# Hàm vẽ hình chữ nhật bo góc (Rounded Rectangle)
def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Vẽ Banner nền tối bo góc ở giữa phía trên
banner_w, banner_h = 400, 50
start_x = (w - banner_w) // 2
start_y = 10
create_rounded_rect(canvas, start_x, start_y, start_x + banner_w, start_y + banner_h, radius=25, fill='#1e1e2e', outline='#00f3ff', width=2)

# Thêm chữ hiển thị trạng thái
text_id = canvas.create_text(start_x + banner_w//2 - 60, start_y + 25, text="🤖 AI Agent is Controlling...", fill='#00f3ff', font=('Segoe UI', 12, 'bold'))

# Tạo nút STOP (Dùng thủ thuật Canvas để đẹp hơn)
stop_btn_x1 = start_x + banner_w - 110
stop_btn_y1 = start_y + 10
stop_btn_x2 = start_x + banner_w - 15
stop_btn_y2 = start_y + 40
btn_bg = create_rounded_rect(canvas, stop_btn_x1, stop_btn_y1, stop_btn_x2, stop_btn_y2, radius=15, fill='#ff4444', outline='')
btn_text = canvas.create_text((stop_btn_x1+stop_btn_x2)//2, (stop_btn_y1+stop_btn_y2)//2, text="🛑 STOP", fill='white', font=('Segoe UI', 10, 'bold'))

# Ràng buộc sự kiện click vào vùng nút STOP
canvas.tag_bind(btn_bg, '<Button-1>', stop_agent)
canvas.tag_bind(btn_text, '<Button-1>', stop_agent)

# Đổi con trỏ khi di chuột vào nút STOP
def on_enter(e):
    canvas.itemconfig(btn_bg, fill='#ff6666')
    root.config(cursor='hand2')

def on_leave(e):
    canvas.itemconfig(btn_bg, fill='#ff4444')
    root.config(cursor='')

canvas.tag_bind(btn_bg, '<Enter>', on_enter)
canvas.tag_bind(btn_text, '<Enter>', on_enter)
canvas.tag_bind(btn_bg, '<Leave>', on_leave)
canvas.tag_bind(btn_text, '<Leave>', on_leave)

# Hiệu ứng nhấp nháy cho chữ để user biết nó đang sống
pulse_state = True
def pulse_text():
    global pulse_state
    color = "white" if pulse_state else "#00f3ff"
    canvas.itemconfig(text_id, fill=color)
    pulse_state = not pulse_state
    root.after(700, pulse_text)

pulse_text()

root.mainloop()
