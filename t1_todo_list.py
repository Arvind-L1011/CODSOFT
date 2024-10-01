import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
tasks = []


def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task")


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")


def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task != "":
            tasks[selected_task_index] = updated_task
            update_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task to update")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update")


def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_label = tk.Label(input_frame, text="Enter the Task:")
task_label.grid(row=0, column=0, columnspan=2, pady=5)

task_entry = tk.Entry(input_frame, width=30)
task_entry.grid(row=1, column=0, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=1, column=1)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, height=8, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

root.mainloop()
