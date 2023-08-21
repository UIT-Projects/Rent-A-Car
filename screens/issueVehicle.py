from components.contentFrame import ContentFrame
from components.headingLabel import HeadingLabel
from components.inputWidget import InputWidgets
from components.buttonSection import ButtonSection
import csv
import pandas as pd
from tabulate import tabulate
import tkinter as tk


def issueVehicle(self):

    self.frame = ContentFrame(self.master)
    HeadingLabel(self.frame, text='Issue Vehicle To Customer')
    input_widget = InputWidgets(self.frame, num_entry_boxes=5)

    def addData():
        data = []
        # Retrieve data from entry boxes
        for entry_box in input_widget.entry_boxes:
            data.append(entry_box.get())
        # Append data to the CSV file
        with open('data/Issue.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)

    def deleteData():
        pass

    def updateData():
        pass

    def showData():
        # Display the added data in a textbox
        data = pd.read_csv('data/Issue.csv')
        formattedData = tabulate(data, headers="keys", tablefmt='plain', showindex=True)
        input_widget.text_area.delete(1.0, tk.END)
        input_widget.text_area.insert('1.0', formattedData)

    showData()

    buttons = [
        ("Add", lambda: [addData(), showData()]),
        ("Delete", lambda: [deleteData(), showData()]),
        ("Update", lambda: [updateData(), showData()]),
        ("QUIT", lambda: [self.frame.destroy()])  # Adding QUIT button to the sidebar
    ]

    button_section = ButtonSection(self.frame)
    button_placement_params = [
        {"relx": 0.6, "rely": 0.95, "relwidth": 0.1, "relheight": 0.05},
        {"relx": 0.7, "rely": 0.95, "relwidth": 0.1, "relheight": 0.05},
        {"relx": 0.8, "rely": 0.95, "relwidth": 0.1, "relheight": 0.05},
        {"relx": 0.9, "rely": 0.95, "relwidth": 0.1, "relheight": 0.05}
    ]
    button_section.create_buttons(buttons, button_placement_params)
