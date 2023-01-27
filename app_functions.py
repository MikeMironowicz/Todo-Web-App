FILEPATH = "to_dos.txt"


def get_todos(filepath=FILEPATH):
    """ returns a to_do list from .txt file"""
    with open(filepath, "r") as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local

def save_todos(to_dos_arg, filepath=FILEPATH):
    """ saves a to_do list to a .txt file"""
    with open(filepath, "w") as file:
        file.writelines(to_dos_arg)


