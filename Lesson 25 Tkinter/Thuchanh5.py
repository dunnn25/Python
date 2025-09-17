"""
Tkinter - delete text, insert text

"""

import tkinter as tk
root = tk.Tk()

my_entry = tk.Entry(bg = "red", fg = "White", width = 10)
my_entry.pack()

# insert text vào entry
my_entry.insert(0, "Hello") # 0 là vị trí index để chèn text vào
# Thêm text vào cuối entry
# my_entry.insert(tk.END,"World")

# # Delete text - xoá text dựa theo chỉ số - first index, last index (Không bao gồm last index)
# my_entry.delete(0,3) # xoá từ vị trí 0 đến vị trí 3 (không bao gồm vị trí 3)
my_entry.delete(0, tk.END) # Xoá tất cả text trong entry

root.mainloop()