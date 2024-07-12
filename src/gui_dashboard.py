import tkinter as tk
from tkinter import font as tkFont
from . import operations


def on_button_click(display_screen, user_input, value):
    if value in "0123456789":
        if user_input.get() == "0" or not user_input.get().isdigit():
            user_input.delete(0, tk.END)
        user_input.insert(tk.END, value)
        display_screen.config(text=display_screen.cget("text") + value)
    elif value in "+-*/":
        if user_input.get().isdigit():
            display_screen.config(text=display_screen.cget("text") + " " + value + " ")
            user_input.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(display_screen.cget("text"))
            user_input.delete(0, tk.END)
            user_input.insert(0, str(result))
            display_screen.config(text=display_screen.cget("text") + " = " + str(result))
        except Exception as e:
            user_input.delete(0, tk.END)
            user_input.insert(0, "Error")
            display_screen.config(text="Error")
    elif value == "C":
        user_input.delete(0, tk.END)
        display_screen.config(text="")

def gui_menu():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x500")
    root.configure(bg='#333333')
    root.resizable(False, False)

    # Fonts
    display_font = tkFont.Font(size=12)
    input_font = tkFont.Font(size=24)

    # Frames
    display_frame = tk.Frame(root, bd=0, relief="flat", bg='#333333')
    display_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Display screen
    display_screen = tk.Label(display_frame, text="", font=display_font, bg='#333333', fg='white', anchor='w')
    display_screen.grid(row=0, column=0, sticky="ew")

    # User input
    user_input = tk.Entry(display_frame, font=input_font, bg='#333333', fg='white', insertbackground='white')
    user_input.grid(row=1, column=0, sticky="ew")

    # Button frame
    button_frame = tk.Frame(root, bg='#003333')
    button_frame.grid(row=1, column=0, sticky="nsew")

    # Buttons
    buttons = [
        '7', '8', '9', '+',
        '4', '5', '6', '-',
        '1', '2', '3', '*',
        'C', '0', '=', '/'
    ]
    row = 0
    col = 0
    for button in buttons:
        action = lambda x=button: on_button_click(display_screen, user_input, x)
        b = tk.Button(button_frame, text=button, command=action, font=input_font, bg="#4D4D4D", fg="white")
        b.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Grid configuration for button layout
    for i in range(4):
        button_frame.grid_columnconfigure(i, weight=1)
        button_frame.grid_rowconfigure(i, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1)

    root.mainloop()