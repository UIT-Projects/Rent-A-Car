import tkinter as tk


class CreateHeader(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="green", bd=5)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.header_label = tk.Label(self, text="Welcome to\nLucifer's Rent A Car",
                                     bg='black', fg='white', font=('Courier', 15))
        self.header_label.place(relx=0, rely=0, relwidth=0.988, relheight=1)
