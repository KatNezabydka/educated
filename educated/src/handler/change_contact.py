from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def change_contact(args: list, book: AddressBook) -> str:
    """
    Change the phone number of an existing contact.

    Parameters:
        args (list): A list containing name and new phone number.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating success or failure.

    Notes:
        If the contact exists, its phone number will be updated with the new one.
        If the contact does not exist, a failure message will be returned.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("New phone number cannot be empty.")
    phone = args[1]

    contact = book.find(name)
    if contact is not None:
        contact.delete_phones().add_phone(phone)
        return f"{Fore.GREEN}Contact updated."
    return f"{Fore.RED}Contact not found."
