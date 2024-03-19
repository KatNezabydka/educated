from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    """
    Show the birthday of a contact.

    Parameters:
        args (list): A list containing the name of the contact.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A string containing the birthday of the contact.

    Notes:
        If the contact exists and has a birthday, its birthday will be returned.
        If the contact does not exist or does not have a birthday, a failure message will be returned.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    record = book.find(name)
    if record is not None:
        if record.has_birthday():
            return record.print_birthday()
        else:
            return f"{Fore.RED}Birthday is empty for this contact."
    return f"{Fore.RED}Contact not found."
