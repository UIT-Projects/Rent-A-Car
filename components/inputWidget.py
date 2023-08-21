import tkinter as tk


class InputWidgets:

    def __init__(self, master, num_entry_boxes=2):
        self.master = master
        self.text_area = tk.Text(master, bg='white', fg='Black', font=('Times new roman', 15))
        self.text_area.place(relx=0, rely=0.11, relwidth=1, relheight=0.7)

        self.input_box = tk.Entry(master)
        self.input_box.place(relx=0, rely=0.85, relwidth=0.13, relheight=0.05)

        self.entry_boxes = []
        for i in range(num_entry_boxes):
            entry = tk.Entry(master)
            entry.place(relx=0.15 * (i + 1), rely=0.85, relwidth=0.13, relheight=0.05)
            self.entry_boxes.append(entry)
