from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    """
    Add birthday to a contact.

    Parameters:
        args (list): A list containing name and birthday.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating success or failure.

    Notes:
        If the contact exists and does not have a birthday yet, the birthday will be added to the contact.
        If the contact does not exist or already has a birthday, a failure message will be returned.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("Birthday cannot be empty.")
    birthday = args[1]

    record = book.find(name)
    if record is not None:
        if record.has_birthday():
            return f"{Fore.YELLOW}Birthday already exists for this contact."
        else:
            record.add_birthday(birthday)
            return f"{Fore.GREEN}✅ Birthday added."
    return f"{Fore.RED}Contact not found."
