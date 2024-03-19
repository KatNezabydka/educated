from educated.src.model.addtess_book.address_book import AddressBook


def birthdays(book: AddressBook) -> None:
    """
    Show upcoming birthdays.

    Parameters:
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        None

    Notes:
        This handler prints upcoming birthdays of contacts within the current week.
        If there are no upcoming birthdays, it prints a message indicating that the list is empty.
    """
    if len(book.data) == 0:
        print("The Address Book is empty")
        return  # Exit the handler early if the address book is empty

    try:
        birthdays_per_week = book.get_birthdays_per_week()
    except Exception as e:
        print(f"Error: {e}")
        return  # Exit the handler if there's an error

    if not any(birthdays_per_week.values()):
        print("No upcoming birthdays within the current week")
        return  # Exit the handler if there are no upcoming birthdays

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")
