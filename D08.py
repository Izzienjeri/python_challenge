import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to add text to the entry
def add_to_expression(value):
    entry.insert(tk.END, value)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget for displaying expressions and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Creating buttons and adding them to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 18), command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="C", font=('Arial', 18), command=clear_entry)
clear_button.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

# Configuring grid to expand with window resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the GUI main loop
root.mainloop()
