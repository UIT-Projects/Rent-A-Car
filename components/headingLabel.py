import tkinter as tk


class HeadingLabel(tk.Label):
    def __init__(self, master=None, text="Default Text"):
        super().__init__(master, text=text, bg='yellow', fg='Black', font=('Courier', 15))
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
