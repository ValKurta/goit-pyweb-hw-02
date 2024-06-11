import unittest
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
from datetime import datetime


def print_after_test(test_name):
    print(f"test {test_name} finished successfully")


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook()

    def test_add_contact(self):
        args = ["V", "1234567890"]
        result = add_contact(args, self.book)
        self.assertEqual(result, "Contact added.")
        self.assertEqual(len(self.book.data), 1)
        self.assertIn("V", self.book.data)
        print_after_test(self._testMethodName)

    def test_add_contact_existing(self):
        args = ["V", "1234567890"]
        add_contact(args, self.book)
        result = add_contact(args, self.book)
        self.assertEqual(result, "Contact updated.")
        self.assertEqual(len(self.book.data), 1)
        self.assertIn("V", self.book.data)
        print_after_test(self._testMethodName)

    def test_change_contact(self):
        add_contact(["V", "1234567890"], self.book)
        result = change_contact(["V", "1234567890", "0987654321"], self.book)
        self.assertEqual(result, "Contact updated.")
        self.assertEqual(str(self.book.data["V"].phones[0]), "0987654321")
        print_after_test(self._testMethodName)

    def test_show_phone(self):
        add_contact(["V", "1234567890"], self.book)
        result = show_phone(["V"], self.book)
        self.assertEqual(result, "1234567890")
        print_after_test(self._testMethodName)

    def test_add_birthday(self):
        add_contact(["V", "1234567890"], self.book)
        result = add_birthday(["V", "01.01.2024"], self.book)
        self.assertEqual(result, "Birthday added.")
        self.assertEqual(str(self.book.data["V"].birthday), "01.01.2024")
        print_after_test(self._testMethodName)

    def test_show_birthday(self):
        add_contact(["V", "1234567890"], self.book)
        add_birthday(["V", "01.01.2024"], self.book)
        result = show_birthday(["V"], self.book)
        self.assertEqual(result, "01.01.2024")
        print_after_test(self._testMethodName)

    def test_birthdays(self):
        add_contact(["V", "1234567890"], self.book)
        today = datetime.today().strftime("%d.%m.%Y")
        add_birthday(["V", today], self.book)
        result = str(self.book.get_upcoming_birthdays())
        self.assertEqual("[{'name': 'V', 'congratulation_date': '2024.06.10'}]", result)
        print_after_test(self._testMethodName)

    def test_delete_contact(self):
        add_contact(["V", "1234567890"], self.book)
        result = delete_contact(["V"], self.book)
        self.assertEqual(result, "Contact V deleted.")
        self.assertNotIn("V", self.book.data)
        print_after_test(self._testMethodName)


if __name__ == "__main__":
    unittest.main()
