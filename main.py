#TODO Account for invalid data
#TODO Exeption handle for runtime errors
#TODO test the code with unit test or pytest
#TODO GUI
#TODO organize with class or modules
#TODO store data in files or database
#TODO ongoing- make sure program is properly documented

def nameAndAge(name: str, age: int) -> str:
    """
    function to return the name and age(multiplied by 2)
    :param name: the name of an indivudal
    :param age: the age of an indivudial
    :return: the name and the age(multiplied by 2)
    """
    return f"Hello {name}! You are {age*2} years old"

def main():
    """
    Main function
    :return:
    """
    name = input("What is your name?").strip().lower().capitalize()
    age = int(input().strip())
    nameAndAge(name, age)

if __name__ == "__main__":
    main()