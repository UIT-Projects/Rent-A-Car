import tkinter as tk


class ContentFrame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='black', bd=5, highlightbackground='green', highlightthickness=4)
        self.place(relx=0.25, rely=0.15, relwidth=0.7, relheight=0.8)
