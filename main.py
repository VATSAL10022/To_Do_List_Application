import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive To-Do List")
        
        self.tasks = []

        # Input Frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.entry_task = tk.Entry(self.input_frame, width=52)
        self.entry_task.pack(side=tk.LEFT, padx=5)

        self.add_task_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, bg="lightblue")
        self.add_task_button.pack(side=tk.LEFT)

        self.complete_task_button = tk.Button(self.input_frame, text="Complete Task", command=self.complete_task, bg="lightgreen")
        self.complete_task_button.pack(side=tk.LEFT)

        self.remove_task_button = tk.Button(self.input_frame, text="Remove Task", command=self.remove_task, bg="salmon")
        self.remove_task_button.pack(side=tk.LEFT)

        # Task List
        self.task_listbox = tk.Listbox(self.root, width=60, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Style the Listbox
        self.task_listbox.config(bg="lightyellow", font=("Arial", 12))

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["text"]
            if task["completed"]:
                display_text = f"✓ {display_text}"  # Mark completed tasks
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
