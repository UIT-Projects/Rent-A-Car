import tkinter as tk
from screens.vehicleInfo import vehicleInfo
from screens.customerInfo import customerInfo
from screens.issueVehicle import issueVehicle
from screens.paymentDetails import paymentDetails
from components.buttonSection import ButtonSection


class CreateSidebar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='black', bd=5, highlightbackground='green', highlightthickness=4)
        self.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.9)

        buttons = [
            ("Customer Info", lambda: [customerInfo(self)]),
            ("Vehicle Info", lambda: [vehicleInfo(self)]),
            ("Issue Vehicle", lambda: [issueVehicle(self)]),
            ("Payment Details", lambda: [paymentDetails(self)]),
            ("QUIT", self.master.quit)  # Adding QUIT button to the sidebar
        ]
        button_placement_params = [
            {"relx": 0.1, "rely": 0.1 * (i + 1), "relwidth": 0.8, "relheight": 0.08} for i in range(len(buttons))
        ]
        button_section = ButtonSection(self)
        button_section.create_buttons(buttons, button_placement_params)
