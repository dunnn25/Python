import tkinter as tk 
root = tk.Tk()

my_entry = tk.Entry(bg = "Black", fg = "White", width = 10)
my_entry.pack()
def on_get():
    entry_text = my_entry.get() # Lấy text từ entry
    print(entry_text)
button = tk.Button(root, text="Get text", command=on_get)
button.pack()


root.mainloop()