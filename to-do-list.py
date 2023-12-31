import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    global entry_task, listbox_tasks

    root = tk.Tk()
    root.title("To-Do List")

    # Create entry widget for tasks
    entry_task = tk.Entry(root, width=50)
    entry_task.pack(pady=10)

    # Create listbox to display tasks
    listbox_tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
    listbox_tasks.pack()

    # Create buttons for adding and deleting tasks
    button_add = tk.Button(root, text="Add Task", command=add_task)
    button_add.pack(pady=5)

    button_delete = tk.Button(root, text="Delete Task", command=delete_task)
    button_delete.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
