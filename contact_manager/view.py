from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def display_contacts(self, contacts: str):
        pass

    @abstractmethod
    def display_birthdays(self, birthdays: list):
        pass

    @abstractmethod
    def display_help(self):
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass


class ConsoleView(View):
    def display_message(self, message: str):
        print(message)

    def display_contacts(self, contacts: str):
        print(f"Contact list:\n{book}")

    def display_contacts(self, contacts: str):
        if not contacts:
            print("Contact list is empty!")
        else:
            print(f"Contact list:\n{contacts}")

    def display_birthdays(self, birthdays: list):
        if not birthdays:
            print("There are no upcoming birthdays.")
        else:
            for day in birthdays:
                print(f"{day}")

    def display_help(self):
        help_message = """
        Available commands:
        - hello: Greet the user.
        - add <name> <phone>: Add a new contact.
        - change <name> <old_phone> <new_phone>: Change a contact's phone number.
        - phone <name>: Show the contact's phone number.
        - all: Show all contacts.
        - add-birthday <name> <birthday>: Add a birthday to a contact.
        - show-birthday <name>: Show the contact's birthday.
        - birthdays: Show upcoming birthdays within a week.
        - close/exit: Exit the application.
        """
        print(help_message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)
