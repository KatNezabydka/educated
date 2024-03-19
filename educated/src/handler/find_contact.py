from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.addtess_book.record import Record
from educated.src.model.validation.validation_error import ValidationError


@input_error
def find_contact(args: list, book: AddressBook) -> Record | str:
    """
    Finds a contact in the address book and updates its information if provided.

    @param args: A list containing contact information in the order: [name].
    @param book: An instance of the AddressBook class.
    @return: A string message indicating the result of the operation.
    @input_error: Indicates potential input errors, such as missing or invalid arguments.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    record = book.find(name)
    if record:
        return record
    return f"{Fore.RED}The contact does not exist, use the 'add-contact' command to create it."
