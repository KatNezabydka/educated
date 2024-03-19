from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.addtess_book.record import Record
from educated.src.model.validation.validation_error import ValidationError


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    """
    Add a new contact to the address book.

    Parameters:
        args (list): A list containing name and phone number.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating success or failure.

    Notes:
        If a contact with the same name already exists in the address book,
        the handler will not add a new contact and return a failure message.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("Phone number cannot be empty.")
    phone = args[1]

    if book.find(name) is None:
        book.add_record(Record(name).add_phone(phone))
        return f"{Fore.GREEN}✅ Contact added."
    return f"{Fore.RED}Contact already exist."
