import tkinter as tk

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Colorful Calculator")

entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0, 'lightblue'), ('8', 1, 1, 'lightblue'), ('9', 1, 2, 'lightblue'), ('/', 1, 3, 'orange'),
    ('4', 2, 0, 'lightblue'), ('5', 2, 1, 'lightblue'), ('6', 2, 2, 'lightblue'), ('*', 2, 3, 'orange'),
    ('1', 3, 0, 'lightblue'), ('2', 3, 1, 'lightblue'), ('3', 3, 2, 'lightblue'), ('-', 3, 3, 'orange'),
    ('0', 4, 0, 'lightblue'), ('.', 4, 1, 'lightblue'), ('+', 4, 2, 'orange'), ('=', 4, 3, 'green'),
]

for (text, row, col, color) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, bg=color, fg="white", font=("Arial", 14), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, bg=color, fg="white", font=("Arial", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

button_clear = tk.Button(root, text="C", padx=40, pady=20, bg="red", fg="white", font=("Arial", 14), command=button_clear)
button_clear.grid(row=5, column=0, columnspan=4)

root.mainloop()
