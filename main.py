from tkinter import *
import re
#TODO Account for invalid data
#TODO Exception handle for runtime errors
#TODO test the code with unit test or pytest
#TODO GUI
#TODO organize with class or modules
#TODO store data in files or database
#TODO ongoing- make sure program is properly documented

class GUI:
    def __init__(self, window):
        """
        creates the GUI
        :param window:
        """
        self.window = window

        self.entry_name = Entry(self.window)
        self.entry_age = Entry(self.window)
        self.label_name = Label(self.window,text="Name:")
        self.label_age = Label(self.window,text="Age:")

        self.label_error = Label(self.window, text="")
        self.button_save = Button(self.window,text="SAVE",command=self.clicked)

        self.label_email = Label(self.window,text="Email")
        self.entry_email = Entry(self.window)
        self.label_phone = Label(self.window,text="Phone #")
        self.entry_phone = Entry(self.window)

        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_age.grid(row=1, column=0)
        self.entry_age.grid(row=1, column=1)
        self.label_error.grid(row=2, column=0)
        self.button_save.grid(row=3, column=1)

        self.label_email.grid(row=4, column=0)
        self.entry_email.grid(row=4, column=1)
        self.label_phone.grid(row=5, column=0)
        self.entry_phone.grid(row=5, column=1)


    def clicked(self):
        """
        gets the name and age variables, clears the text box
        :return: none
        """
        self.label_error.config(text="")
        if self.entry_name.get()=="" or self.entry_age.get()=="" or self.entry_email.get()=="" or self.entry_phone.get()=="":
            self.label_error.config(text="please fill all inputs")
        else:
            try:
                int(self.entry_age.get())
                if int(self.entry_age.get()) <= 0:
                    raise ValueError
            except ValueError:
                self.label_error.config(text="Please put in a + integer for age")
                self.label_error.grid(row=4,column=1) #FIXME need to change this to what is said when originally placing
            else:
                if checkemail(self.entry_email.get()):
                    if checkphone(self.entry_phone.get()):
                        agegui = self.entry_age.get()
                        namegui = self.entry_name.get()
                        emailgui = self.entry_email.get()
                        phonegui = self.entry_phone.get()
                        # print(nameAndAge(namegui, int(agegui),emailgui))
                        self.entry_name.delete(0, END)
                        self.entry_age.delete(0, END)
                        self.entry_email.delete(0, END)
                        self.entry_phone.delete(0, END)
                else:
                    self.label_error.config(text="please put in a valid email")

def nameAndAge(name: str, age: int, email: str) -> str:
    """
    function to return the name and age(multiplied by 2)
    :param name: the name of an individual
    :param age: the age of an individual
    :return: the name and the age(multiplied by 2)
    """
    with open("namesAndAges.txt","a") as f:
        f.write(f"Name: {name}, Age: {age*2}")
    return (f"Hello {name}! You are {age*2} years old.")

def checkemail(email):
    """
    checks if email is valid with regular expressions
    tests if alphanumeric and some symbols first, followed by the @ symbol, then period, and then 2 or more alphabetic characters
    :param email:
    :return: true if vaild, false if not vaild
    """
    if (re.fullmatch)(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email):
        return True
    else:
        return False

def checkphone(phonenumber):
    """
    checks if phone number is vaild with regular expressions
    test if 0-9 in a group of three, another group of 0-9 in three and then 0-9 in four, will work with dashes and periods, and parenthesis around the first three
    :param phonenumber:
    :return: true if valid, false if not
    """
    if (re.fullmatch)("^\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})$",phonenumber):
        return True
    else:
        return False

def main():
    """
    Main function
    :return:
    """
    window = Tk()
    window.title("Project 1")
    window.geometry("500x500")
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()