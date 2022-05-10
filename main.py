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
        self.label_error.grid(row=7, column=1)  ##########
        self.button_save.grid(row=6, column=1)

        self.label_email.grid(row=2, column=0)
        self.entry_email.grid(row=2, column=1)
        self.label_phone.grid(row=3, column=0)
        self.entry_phone.grid(row=3, column=1)

        self.genders=["please choose", "Male", "Female", "Other"]
        self.gendervar = StringVar()
        self.gendervar.set(self.genders[0])

        self.dropdown =OptionMenu(self.window,self.gendervar, *self.genders)
        self.dropdown.grid(row=5, column=1)
        self.label_gender = Label(self.window,text="Gender")
        self.label_gender.grid(row=5, column=0)


    def clicked(self):
        """
        gets the name and age variables, clears the text box
        :return: none
        """
        self.label_error.config(text="")
        self.isready=0
        self.errormsg=""
        if self.entry_name.get()=="" or self.entry_age.get()=="" or self.entry_email.get()=="" or self.entry_phone.get()=="" or self.gendervar.get()=="please choose":
            self.label_error.config(text="please fill all inputs")
        else:
            ### age  ↓
            try:
                int(self.entry_age.get())
                if int(self.entry_age.get()) <= 0:
                    raise ValueError
            except ValueError:
                self.errormsg=self.errormsg+"Please put in a + integer for age "
                self.label_error.config(text=self.errormsg)
                self.label_error.grid(row=7, column=1)  # FIXME need to change this to what is said when originally placing
            else:
                self.isready+=1
            ### age  ↑
            ### email ↓
            if checkemail(self.entry_email.get()):
                self.isready+=1
            else:
                self.errormsg=self.errormsg+"please put in a valid email "
                self.label_error.config(text=self.errormsg)
            ### email ↑
            ### phone ↓
            if checkphone(self.entry_phone.get()):
                self.isready+=1
            else:
                self.errormsg=self.errormsg+"please put in a valid phone number"
                self.label_error.config(text=self.errormsg)
            ### phone ↑

            if self.isready == 3:
                print(toWrite(self.entry_name(),int(self.entry_age.get()),self.entry_email.get(),self.entry_phone.get(),self.gendervar.get()))
                self.entry_name.delete(0, END)
                self.entry_age.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_phone.delete(0, END)
                self.dropdown.set(self.genders[0]) #FIXME need to clear dropdown, this doesnt work

def toWrite(name: str, age: int, email: str, phone, gender):
    """
    function to return the name and age(multiplied by 2)
    :param name: the name of an individual
    :param age: the age of an individual
    """
    with open("namesAndAges.txt","a") as f:
        f.write(f"Name: {name}, Age: {age}, Email: {email}, phone #: {phone}, gender: {gender}")
        return f"Name: {name}, Age: {age}, Email: {email}, phone #: {phone}, gender: {gender}"

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
    window.geometry("600x250")
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()