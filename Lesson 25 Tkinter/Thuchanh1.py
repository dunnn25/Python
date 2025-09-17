import tkinter as tk

root = tk.Tk()
def on_click():
    print("Wowwwwwww")
button = tk.Button(root, text="Click", command=on_click) # command là khi chúng ta nhấn vào button thì hàm on_click sẽ thực hiện
button.pack()


# event (sự kiện) ở đây là hành động nhấn vào button
# callback function (hàm gọi lại) là hàm on_click
root.mainloop()