from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.entry_name = Entry(self.window)
        self.entry_age = Entry(self.window)
        self.label_error = Label(self.window, text="")
        self.button_save = Button(self.window,text="SAVE",command=self.clicked)

        self.entry_name.pack(side="top")
        self.entry_age.pack(side="top")
        self.label_error.pack(side="top")
        self.button_save.pack(side="top")

    def clicked(self):
        if type(self.entry_name) != str:
            self.label_error.config
        name = self.entry_name.get()
        age = self.entry_age.get()
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
