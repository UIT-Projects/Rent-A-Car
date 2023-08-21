from components.header import CreateHeader
from components.slideBar import CreateSidebar
import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Rent A Car")
        self.minsize(width=400, height=400)
        self.geometry(str(self.winfo_screenwidth()) + "x" + str(self.winfo_screenheight()))
        self.image = tk.PhotoImage(file='image/bg.app.png')
        self.bg = tk.Label(self, image=self.image, )
        self.bg.place(relx=0.14, rely=0, relwidth=1, relheight=1.1)

        CreateHeader(self)
        CreateSidebar(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
