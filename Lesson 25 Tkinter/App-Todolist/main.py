import tkinter as tk
from tkcalendar import DateEntry



root = tk.Tk()
root.title("To-Do List")
root.geometry("500x300")

class DateSelector:
    def __init__(self, master):
        self.master = master
        self.cal = DateEntry(master, selectmode='day')
        self.cal.pack(pady=20)
        self.button = tk.Button(master, text="Get Selected Date", command=self.get_selected_date)
        self.button.pack(pady=10)
    def get_selected_date(self):
        selected_date = self.cal.get_date()
        # print(f"Selected Date: {selected_date}")
        pass
class TaskManager:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)
        self.entry = tk.Entry(self.frame, width=40)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        self.listbox = tk.Listbox(master, width=50, height=10)
        self.listbox.pack(pady=10)
        self.delete_button = tk.Button(master, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            # self.entry.delete(0, tk.END)
    def delete_task(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            self.listbox.delete(index)
            del self.tasks[index]


date_selector = DateSelector(root)
task_manager = TaskManager(root)
def complete_task():
    date_selector.get_selected_date()
    print(f"Tasks: {task_manager.tasks} on {date_selector.cal.get_date()}")
button = tk.Button (root, text = "Complete Task", command=complete_task)
button.pack(pady=10)
root.mainloop()