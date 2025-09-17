import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# thêm một cái widget là button
button = tk.Button(root, text="Click me")
button1 = tk.Button(root, text="Click me1")

button.pack() # hiển thị button lên cửa sổ chính
button1.pack()
root.mainloop()     # giữ cho cửa sổ mở cho đến khi người dùng đóng nó