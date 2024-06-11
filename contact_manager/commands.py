from addressbook import AddressBook
from models import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Name not found. Please, check and try again."
        except ValueError as e:
            return e
        except IndexError:
            return "Enter correct information."
    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def delete_contact(args, book: AddressBook):
    if len(args) < 1:
        return "Not enough arguments. Usage: delete <name>"
    name = args[0]
    book.delete(name)
    return f"Contact {name} deleted."


@input_error
def change_contact(args, book):
    try:
        name, old_phone, new_phone, *_ = args
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            return "Contact updated."
        else:
            raise KeyError
    except KeyError:
        raise KeyError("Contact not found.")


@input_error
def show_phone(args, book):
    (name,) = args
    record = book.find(name)
    if record:
        return "; ".join([str(phone) for phone in record.phones])
    else:
        raise KeyError


def show_all(book):
    return "\n".join([str(record) for record in book.data.values()])


@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError


@input_error
def show_birthday(args, book):
    (name,) = args
    record = book.find(name)
    return str(record.birthday)
