import tkinter as tk
from tkinter import messagebox  
# tạo cửa sổ chính
root = tk.Tk()

# Set tiêu đề cho chương trình 
root.title("Chuyển độ C sang độ F")

# Cố định kích thước cửa sổ 
root.geometry("500x500")  # width x height

# Label hướng dẫn
label_tur = tk.Label(root, text="Chuyển độ C sang độ F", font="Times 20 bold", fg="blue")
label_tur.pack(pady=10)

# Entry để nhập độ C
entry_c = tk.Entry(root, font="Times 13", fg="red", width=20)
entry_c.pack(pady=10)
entry_c.insert(0, "0")

# Callback function - hàm chuyển đổi độ C sang độ F
def convert_c_to_f():
    try:
        # Lấy giá trị từ entry
        celsius = float(entry_c.get())
        fahrenheit = (celsius * 1.8) + 32
        label_dis.config(text=f"Độ F là: {fahrenheit:.2f} °F")
    except ValueError:
        # print("Vui lòng nhập số hợp lệ")
        messagebox.showerror(title="Error", message="Vui lòng nhập số hợp lệ")

# Button chuyển đổi
button_convert = tk.Button(root, text="Change", font="Times 13 bold", bg="white", fg="blue", command=convert_c_to_f)
button_convert.pack(pady=5)

# Label hiển thị 
label_dis = tk.Label(root, text="Độ F là: ", font="Times 15 bold")
label_dis.pack(pady=10)

# giữ cho cửa sổ mở cho đến khi đóng
root.mainloop()
