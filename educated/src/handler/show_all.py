from colorama import Fore

from educated.src.model.addtess_book.address_book import AddressBook


def show_all(book: AddressBook) -> print:
    """
    Show all contacts in the address book.

    Parameters:
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        None

    Notes:
        This handler prints information about all contacts in the address book.
        If the address book is empty, it prints a message indicating that.
    """

    if len(book.data) == 0:
        print(Fore.RED + "The list is empty" + " ¯\\_(ツ)_/¯")
        return

    for name, record in book.data.items():
        print(
            f"👤 {name}. {record.print_birthday()} {record.print_phones()} {record.print_emails()} {record.print_addresses()}"
        )
