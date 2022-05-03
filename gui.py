from tkinter import *
"""
class GUI:
    def __init__(self, window):
        """
        creates the GUI
        :param window:
        """
        self.window = window

        self.entry_name = Entry(self.window)
        self.entry_age = Entry(self.window)
        self.label_error = Label(self.window, text="")

        self.button_save = Button(self.window,text="SAVE",command=self.clicked)
        self.label_name = Label(self.window,text="Name:")
        self.label_age = Label(self.window,text="Age:")

        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_age.grid(row=1, column=0)
        self.entry_age.grid(row=1, column=1)
        self.label_error.grid(row=2, column=0)
        self.button_save.grid(row=3, column=1)


    def clicked(self):
        """
        gets the name and age variables, clears the text box
        :return: none
        """
        self.label_error.config(text="")
        if self.entry_name.get()=="" or self.entry_age.get()=="":
            self.label_error.config(text="please fill all inputs")
        else:
            try:
                int(self.entry_age.get())
                if int(self.entry_age.get()) <= 0:
                    raise ValueError
            except ValueError:
                self.label_error.config(text="Please put in a + integer for age")
                self.label_error.grid(row=4,column=1)
            else:
                agegui = self.entry_age.get()
                namegui = self.entry_name.get()
                self.entry_name.delete(0, END)
                self.entry_age.delete(0, END)
