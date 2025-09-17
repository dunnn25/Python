"""
Button (Chứa text và thực hiện action)
"""

import tkinter as tk
root = tk.Tk()

# đi tạo 1 function để thực hiện khi nhấn button
def on_click():
    print("Wowwwwwww")

# THay đổi màu sắc của nền - background - bg
# THay đổi màu sắc của chữ - foreground - fg
# THay đổi độ rộng - width, chiều cao - height
button = tk.Button(root, text="Click nne", bg="Red", fg="White",width = 20, height=5, command=on_click) # command là khi chúng ta nhấn vào button thì hàm on_click sẽ thực hiện
button.pack()




root.mainloop()    
    