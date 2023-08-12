# Import the tkinter library for creating GUI Applications
import tkinter as tk

# Import specific widgets and classes from tkinter
from tkinter import ttk, messagebox

# Import the style class from ttkbootstrap for customizing the UI appearance
from ttkbootstrap import Style

# Import the Json library for working with Json data
import json

class TodoListApp(tk.Tk):
    def __init__(self):
# Call the constructor of the parent class (tk.Tk) to initialize the base functionality of a Tkinter application
        super().__init__()

# Intialize the Application Window
        self.title("Todo List App")
        self.geometry("400x400")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground="mediumvioletred")

        # Create input field for adding tasks
        self.task_input = ttk.Entry(self, font=(
            "TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.task_input.pack(pady=10)

        # Set placeholder for input field
        self.task_input.insert(0, "Enter your todo here...")

        # Bind event to clear placeholder when input field is clicked
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        # Bind event to restore placeholder when input field loses focus
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        # Create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.task_list = tk.Listbox(self, font=(
            "TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", style="success.TButton",
                   command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton",
                   command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Create buttton for displaying task statistics
        ttk.Button(self, text="View Stats", style="info.TButton",
                   command=self.view_stats).pack(side=tk.BOTTOM, pady=10)
        
        self.load_tasks()
    
    def view_stats(self):
        # Calculate and display task statistics in a messagebox
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        # Add a new task to the listbox and set text color to orange
        task = self.task_input.get()
        if task != "Enter your todo here...":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        # Mark the selected task as done by changing text color to green
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()
    
    def delete_task(self):
        # Delete the selected task from the listbox
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
    
    def clear_placeholder(self, event):
        # Clear the placeholder text when input field is clicked
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        # Restore the placeholder text when input field loses focus
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        # Load tasks and their colors from the file
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        # Save the tasks and their colors to a file
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()