import tkinter as tk


class ButtonSection:
    def __init__(self, master):
        self.master = master

    def create_buttons(self, buttons, placement_params):
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.master, text=text, bg='black', fg='white', bd=5, command=command)
            btn.place(**placement_params[i])

            if text == "QUIT":
                btn.config(bg='red')
