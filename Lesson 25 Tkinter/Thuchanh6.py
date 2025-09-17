import tkinter as tk

# tạo cửa sổ chính
root = tk.Tk()

def on_click():
    # # Cách sử dụng index trong Text widget
    # # "1.0" - dòng 1, ký tự 0 (bắt đầu từ 0)
    # # "2.3" - dòng 2, ký tự 3
    # # "end" - kết thúc văn bản
    # my_text = tex_box.get("1.0", tk.END)
    #-------------------------------------------
    # # Lấy ký tự đầu tiên ở dòng đầu tiên
    # my_text = tex_box.get("1.0","1.3")
    #-------------------------------------------
    # Lấy toàn bộ dòng đầu tiên
    my_text = tex_box.get("1.0","1.end")
    print(my_text)

label = tk.Label(root, text="Nhập nội dung vào bên dưới:")
label.pack()

tex_box = tk.Text(root, font=("Arial", 12), height=10, width=40)
tex_box.pack()

button = tk.Button(root, text="Nhập",bg="red" ,command=on_click)
button.pack()



# Giũ cho cửa sổ mở cho đến khi đóng
root.mainloop()