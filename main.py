import gui
from gui import *
#TODO Account for invalid data
#TODO Exception handle for runtime errors
#TODO test the code with unit test or pytest
#TODO GUI
#TODO organize with class or modules
#TODO store data in files or database
#TODO ongoing- make sure program is properly documented


def nameAndAge(name: str, age: int) -> str:
    """
    function to return the name and age(multiplied by 2)
    :param name: the name of an individual
    :param age: the age of an individual
    :return: the name and the age(multiplied by 2)
    """
    with open("namesAndAges.txt","a") as f:
        f.write(f"{name}, {age}")
    return (f"Hello {name}! You are {age*2} years old.")

def main():
    """
    Main function
    :return:
    """
    window = Tk()
    window.title("Project 1")
    window.geometry("230x105")
    window.resizable(False, False)

    widgets = gui.GUI(window)
    window.mainloop()

    name = namegui #FIXME need to get name from gui
    age = agegui #FIXME need to get age from gui
    print(nameAndAge(name,age))


if __name__ == "__main__":
    main()