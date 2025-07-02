import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
# Entry for user input
task_input = tk.Entry(root, width=30)
task_input.pack(pady=10)

# Listbox to show tasks
task_listbox = tk.Listbox(root, height=15, width=40)
task_listbox.pack()

# Buttons
def add_task():
    task = task_input.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)
FILENAME = "tasks.txt"

def save_tasks():
    with open(FILENAME, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())
load_tasks()
root.mainloop()
