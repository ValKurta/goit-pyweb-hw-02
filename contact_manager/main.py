import pickle
from addressbook import AddressBook
from view import ConsoleView
from utils import parse_input, load_data, file_path
from commands import (
    add_contact,
    delete_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday
)


def main():
    book = load_data()
    view = ConsoleView()
    view.display_message("Welcome to the assistant bot!")
    while True:
        user_input = view.get_input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            view.display_message("Good bye!")
            with open(file_path, "wb") as file:
                pickle.dump(book, file)
            break
        elif command == "hello":
            view.display_message("How can I help you?")
        elif command == "add":
            view.display_message(add_contact(args, book))
        elif command == "delete":
            view.display_message(delete_contact(args, book))
        elif command == "change":
            view.display_message(change_contact(args, book))
        elif command == "phone":
            view.display_message(show_phone(args, book))
        elif command == "all":
            view.display_contacts(show_all(book))
        elif command == "add-birthday":
            view.display_message(add_birthday(args, book))
        elif command == "show-birthday":
            view.display_message(show_birthday(args, book))
        elif command == "birthdays":
            view.display_birthdays(book.get_upcoming_birthdays())
        else:
            view.display_message("Invalid command.")


if __name__ == "__main__":
    main()
