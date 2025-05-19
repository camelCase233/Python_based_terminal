import tkinter as tk
import real_deal as cmd
import shlex



def run():
    window = tk.Tk()
    window.geometry('200x200')
    label = tk.Label(text="Terminal", bg="black", fg="white")
    e = tk.Entry()
    e.pack()

    def button_press():
        if shlex.split(e.get())[0] == 'ls':
            cmd.

    window.update_idletasks()
    label.update_idletasks()

    window_width = window.winfo_width()
    label_width = label.winfo_width()

    x = (window_width-label_width) // 2

    label.place(x=x)

    return window
