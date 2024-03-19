from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def show_phone(args: list, book: AddressBook) -> str:
    """
    Show the phone numbers of a contact.

    Parameters:
        args (list): A list containing the name of the contact.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A string containing the phone numbers of the contact.

    Notes:
        If the contact exists, its phone numbers will be printed.
        If the contact does not exist, a failure message will be returned.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    contact = book.find(name)
    if contact is not None:
        return contact.print_phones()
    return f"{Fore.RED}Contact not found."
