import tkinter as tk
from tkinter import messagebox
import os

# Window setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

# Entry box
task_input = tk.Entry(root, width=30)
task_input.pack(pady=10)

# Task list
task_listbox = tk.Listbox(root, height=15, width=40)
task_listbox.pack()

# File to store tasks
FILENAME = "tasks.txt"

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

# Add task
def add_task():
    task = task_input.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Delete task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)

# Load existing tasks
load_tasks()

# Run app
root.mainloop()
