import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6 characters.")
            return

        complexity = complexity_var.get()

        if complexity == 1:
            characters = string.ascii_lowercase
        elif complexity == 2:
            characters = string.ascii_letters
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            messagebox.showerror("Error", "Invalid complexity level.")
            return

        global password
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated password: {password}")

        copy_button.config(state="normal")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")


def copy_password():
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

length_label = tk.Label(root, text="Enter the desired length of the password (minimum 6):")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

complexity_label = tk.Label(root, text="Choose password complexity level:")
complexity_label.pack(pady=10)

complexity_var = tk.IntVar()
complexity_var.set(1)

low_complexity = tk.Radiobutton(root, text="Low (lowercase letters)", variable=complexity_var, value=1)
low_complexity.pack(anchor="w", padx=20)

medium_complexity = tk.Radiobutton(root, text="Medium (lowercase and uppercase letters)", variable=complexity_var,
                                   value=2)
medium_complexity.pack(anchor="w", padx=20)

high_complexity = tk.Radiobutton(root, text="High (letters, digits, and special characters)", variable=complexity_var,
                                 value=3)
high_complexity.pack(anchor="w", padx=20)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, state="disabled")
copy_button.pack(pady=10)

root.mainloop()
