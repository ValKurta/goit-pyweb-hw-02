import pickle
from pathlib import Path
from addressbook import AddressBook

file_path = Path("database.bin")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def load_data():
    if file_path.is_file():
        with open(file_path, "rb") as file:
            return pickle.load(file)
    else:
        return AddressBook()
