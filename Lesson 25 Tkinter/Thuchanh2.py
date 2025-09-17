"""
Tkinter - Label (hiện thị text, ảnh)
"""

 
import tkinter as tk
root = tk.Tk()

# label = tk.Label(root, text="Hello World")
# Làm sao để tuỳ chỉnh label
"""Đơn vị của chiều rộng: theo chiều rộng của số 0
Đơn vị của chiều cao: theo chiều cao của số 0
"""
label = tk.Label(root, text="Hello world", fg="Blue",bg="Yellow", width=15, height=15)
label.pack()
label1 = tk.Label(root, text="Chào mừng mọi người", font=("Arial", 24, "bold italic"), fg="red")
label1.pack()


root.mainloop()