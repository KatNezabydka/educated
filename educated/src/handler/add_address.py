from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def add_address(args: list, book: AddressBook) -> str:
    """
    Add address to a contact.

    Parameters:
        args (list): A list containing name and address components.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating success or failure.

    Notes:
        If the contact already exists, the address will be added to the existing contact.
        If the contact does not exist, a new contact will be created.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("Address cannot be empty.")
    address = " ".join(map(str, args[1:]))

    record = book.find(name)
    if record and record.has_address() is False:
        record.add_address(address)
        book.add_record(record)
        return f"{Fore.GREEN}✅ Address added."
    return f"{Fore.RED}The contact does not exist, or already has address."
