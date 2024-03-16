from collections import defaultdict
from colorama import init, Fore, Style, Back
from prompt_toolkit import prompt
from datetime import datetime, timedelta

from educated.src.AddressBook import AddressBook
from educated.src.ValidationError import ValidationError
from educated.src.NoteBook import NoteBook
from educated.src.Faker.user_management import load_or_generate_users, save_users
from educated.src.Faker.note_management import load_or_generate_notes, save_notes
from educated.src.CustomCompleter.CustomCompleter import CustomCompleter, custom_style
from educated.src.Note import Note
from educated.src.Record import Record

completer = CustomCompleter()


def prompt_with_completion():
    text = prompt("Enter a command: ", style=custom_style, completer=completer)
    return text


def input_error(func):
    """
    Decorator to handle input errors gracefully.

    This decorator catches exceptions that occur within the decorated function.
    If an exception occurs, it looks up an appropriate error message based on the type of the exception
    and returns it. If no specific error message is found, it re-raises the exception.

    Parameters:
        func: The function to be decorated.

    Returns:
        The decorated function.

    Notes:
        This decorator is useful for handling errors that may occur due to invalid input.
        It provides a way to customize error messages for specific exception types.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return str(e)
        except Exception as e:
            if not callable(e):
                return str(e)
            else:
                raise e

    return inner


def show_help():
    """
    Print available commands with color highlighting
    """
    print("*" * 30 + " < HELP MENU START > " + "*" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "Available commands:")
    print(Fore.YELLOW + "--> hello: Get a greeting from the bot.")
    print(Fore.YELLOW + "--> add [name] [phone]: Add a new contact with the name and phone number.")
    print(Fore.YELLOW + "--> add-address [name] [address]: Add an address for the specified contact.")
    print(Fore.YELLOW + "--> add-email [name] [email]: Add an email address for the specified contact.")
    print(Fore.YELLOW + "--> change [name] [new phone]: Change the phone number for the specified contact.")
    print(Fore.YELLOW + "--> phone [name]: Show the phone number for the specified contact.")
    print(Fore.YELLOW + "--> find_contact: [name] show all information about person")
    print(Fore.YELLOW + "--> show-all: Show all contacts in the address book.")
    print(Fore.YELLOW + "--> add-birthday [name] [birthday]: Add a birthday for the specified contact.")
    print(Fore.YELLOW + "--> show-birthday [name]: Show the birthday for the specified contact.")
    print(Fore.YELLOW + "--> show-all-birthdays [days]: Show birthdays happening within the specified number of days.")
    print(Fore.YELLOW + "--> birthdays: Show birthdays happening within the next week.")
    print(Fore.YELLOW + "--> add-note [note]: Add a note to the note book.")
    print(Fore.YELLOW + "--> edit-note-content [note_id] [new_content]: Edit the content of a note.")
    print(Fore.YELLOW + "--> delete-note [note_id]: Delete a note from the note book.")
    print(Fore.YELLOW + "--> show-note [note_id]: Show the content of a note by its ID.")
    print(Fore.YELLOW + "--> show-all-notes: Show all notes in the note book, sorted by name.")
    print(Fore.YELLOW + "--> show-notes-tag [tag]: Show notes in the note book by tag.")
    print(Fore.YELLOW + "--> show-all-notes-tag: Show all notes in the note book, sorted by tag.")
    print(Fore.RED + "--> close or exit: Close the program.")
    print("*" * 30 + " < HELP MENU END > " + "*" * 30)
    print(Style.RESET_ALL)  # Reset colors


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


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
        the function will not add a new contact and return a failure message.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("Phone number cannot be empty.")
    phone = args[1]

    if book.find(name) is None:
        book.add_record(Record(name).add_phone(phone))
        return f"{Fore.GREEN} ✅ Contact added."
    return f"{Fore.YELLOW} Contact already exist."


@input_error
def add_email(args: list, book: AddressBook) -> str:
    """
    Add email to a contact.

    Parameters:
        args (list): A list containing name and email.
        book (AddressBook): An instance of AddressBook class.

    Returns:
        str: A message indicating success or failure.

    Notes:
        If the contact already exists, the email will be added to the existing contact.
        If the contact does not exist, a new contact will be created.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    if len(args) == 1:
        raise ValidationError("Email cannot be empty.")
    email = args[1]

    record = book.find(name)
    if record:
        record.add_email(email)
        book.add_record(record)
        return f"{Fore.GREEN} ✅ Email added."
    return f"{Fore.YELLOW} The contact does not exist, use the 'add' command to create it."


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
    if record:
        record.add_address(address)
        book.add_record(record)
        return f"{Fore.GREEN} ✅ Address added."
    return f"{Fore.YELLOW} The contact does not exist, use the 'add' command to create it."


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
        return f"{Fore.GREEN} Contact updated."
    return f"{Fore.RED} Contact not found."


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
    return f"{Fore.RED} Contact not found."


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
    return f"{Fore.YELLOW} The contact does not exist, use the 'add' command to create it."


def show_all(book: AddressBook) -> print:
    """
    Show all contacts in the address book.

    Parameters:
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        None

    Notes:
        This function prints information about all contacts in the address book.
        If the address book is empty, it prints a message indicating that.
    """

    if len(book.data) == 0:
        print(Fore.RED + "The list is empty" + " ¯\\_(ツ)_/¯")
        return

    for name, record in book.data.items():
        print(
            f"👤 {name}. {record.print_birthday()} {record.print_phones()} {record.print_emails()} {record.print_addresses()}")


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
            return f"{Fore.YELLOW} Birthday already exists for this contact."
        else:
            record.add_birthday(birthday)
            return f"{Fore.GREEN} ✅ Birthday added."
    return f"{Fore.YELLOW} Contact not found."


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
            return f"{Fore.YELLOW} Birthday is empty for this contact."
    return f"{Fore.YELLOW} Contact not found."


@input_error
def show_birthdays_within_days(args, book: AddressBook) -> str:
    """
    Show birthdays of contacts within specified days.

    Parameters:
        args: The number of days to check for upcoming birthdays.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A string containing all the found upcoming birthdays.

    Notes:
        This function prints the birthdays of contacts that fall within the specified number of days
        from the current date.
    """

    if len(args) == 0:
        raise ValidationError("Number of days must be provided.")

    try:
        days = int(args[0])
    except ValueError:
        raise ValidationError("Number of days must be an integer.")

    today = datetime.now().date()
    end_date = today + timedelta(days=days)

    birthdays_within_days = []
    for name, contact in book.items():
        birthday = contact.get_birthday()

        if birthday:
            today = datetime.now().date()
            birthday_this_year = datetime(today.year, birthday.value.month, birthday.value.day)
            if birthday_this_year.date() < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year.date() <= end_date:
                days_until_birthday = (birthday_this_year.date() - today).days

                if days_until_birthday == 0:
                    days_until_str = "(today)"
                elif days_until_birthday == 1:
                    days_until_str = "(tomorrow)"
                else:
                    days_until_str = f"(in {days_until_birthday} days)"

                birthdays_within_days.append(
                    f"{Fore.BLUE}📅{birthday_this_year.strftime('%d.%m.%Y')} {days_until_str} - {Fore.GREEN}👤{name}")
    if len(birthdays_within_days) == 0:
        return f"No upcoming birthdays within the {days} days found"
    return '\n'.join(birthdays_within_days)


def birthdays(book: AddressBook) -> None:
    """
    Show upcoming birthdays.

    Parameters:
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        None

    Notes:
        This function prints upcoming birthdays of contacts within the current week.
        If there are no upcoming birthdays, it prints a message indicating that the list is empty.
    """
    if len(book.data) == 0:
        print("The Address Book is empty")
        return  # Exit the function early if the address book is empty

    try:
        birthdays_per_week = book.get_birthdays_per_week()
    except Exception as e:
        print(f"Error: {e}")
        return  # Exit the function if there's an error

    if not any(birthdays_per_week.values()):
        print("No upcoming birthdays within the current week")
        return  # Exit the function if there are no upcoming birthdays

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


@input_error
def add_note(args: list, note_book: NoteBook) -> str:
    """
    Add a note to the notebook.

    Parameters:
        args (list): A list containing name, tag, and content of the note.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A message indicating success.

    Notes:
        This function adds a note to the notebook with the provided name, tag, and content.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    tag = None
    if len(args) > 1:
        tag = args[1]

    content = " ".join(args[2:])
    if note_book.find(name) is None:
        note_book.add_note(Note(name, tag, content))
        return f"{Fore.GREEN} ✅ Note added."
    return f"{Fore.YELLOW}Note with the same name already exists."


@input_error
def edit_note_content(args: list, note_book: NoteBook) -> str:
    """
    Edit the content of a note.

    Parameters:
        args (list): A list containing name of the note and the new content.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A message indicating success.

    Notes:
        This function edits the content of a note identified by its name and updates it with the new content.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    new_content = " ".join(args[1:])
    note_book.edit_note_content(name, new_content)
    return "✅ Note content updated."


@input_error
def edit_note_tag(args: list, note_book: NoteBook) -> str:
    """
    Edit the tag of a note.

    Parameters:
        args (list): A list containing name of the note and the new tag.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A message indicating success.

    Notes:
        This function edits the tag of a note identified by its name and updates it with the new tag.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    new_tag = None
    if len(args) > 1:
        new_tag = args[1]

    note_book.edit_note_tag(name, new_tag)
    return "✅ Note tag updated."


@input_error
def delete_note(args: list, note_book: NoteBook) -> str:
    """
    Delete a note from the notebook.

    Parameters:
        args (list): A list containing the name of the note to be deleted.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A message indicating success.

    Notes:
        This function deletes a note from the notebook based on its name.
    """
    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    note_book.delete_note(name)
    return "✅ Note deleted."


@input_error
def show_note_by_name(args: list, note_book: NoteBook) -> str:
    """
    Show a note by its name.

    Parameters:
        args (list): A list containing the name of the note to be displayed.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A string containing the content of the note.

    Notes:
        This function retrieves and returns the content of a note from the notebook based on its name.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]
    return note_book.show_by_name(name)


@input_error
def show_all_notes_sorted_by_name(note_book: NoteBook) -> str:
    """
    Show all notes sorted by name.

    Parameters:
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A string containing all notes sorted by name.

    Notes:
        This function retrieves all notes from the notebook and returns them as a string, sorted by name.
    """
    return note_book.show_all_sorted_by_name()


@input_error
def show_notes_by_tag(args: list, note_book: NoteBook) -> str:
    """
    Show notes by tag.

    Parameters:
        args (list): A list containing the tag of the notes to be displayed.
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A string containing the notes with the specified tag.

    Notes:
        This function retrieves and returns the notes from the notebook based on their tag.
    """
    if len(args) == 0:
        raise ValidationError("Tag cannot be empty.")
    tag = args[0]
    return note_book.show_by_tag(tag)


@input_error
def show_all_notes_sorted_by_tag(note_book: NoteBook) -> str:
    """
    Show all notes sorted by tag.

    Parameters:
        note_book (NoteBook): An instance of the NoteBook class.

    Returns:
        str: A string containing all notes sorted by tag.

    Notes:
        This function retrieves all notes from the notebook and returns them as a string, sorted by tag.
    """
    return note_book.show_all_sorted_by_tag()


def main():
    # Initialize colorama for color support in the console
    init(autoreset=True)

    book = AddressBook()
    note_book = NoteBook()
    commands_to_close = ["close", "exit"]
    print(
        Back.WHITE
        + Fore.BLACK
        + Style.BRIGHT
        + "🌟 Welcome to the assistant bot! 🌟 Type "
        + Back.GREEN
        + "help"
        + Back.WHITE
        + " for assistance."
    )

    # Load or generate fake users
    users_data = load_or_generate_users()

    # Add fake users to the address book
    for user in users_data:
        fake_user = Record(user["name"])
        fake_user.add_phone(user["phone"])
        if user["birthday"] is not None:
            fake_user.add_birthday(user["birthday"])
        book.add_record(fake_user)

    # Load or generate notes
    notes_data = load_or_generate_notes()
    # Add notes to the notebook
    for note in notes_data:
        note_book.add_note(Note(note["name"], note["tag"], note["content"]))

    while True:
        """
        Running the console with autocompletion
        """
        user_input = prompt_with_completion()
        command, *args = parse_input(user_input)

        match command:
            case "help":
                show_help()
            case "hello":
                print(Fore.CYAN + "How can I help you? 😊")
            case "add":
                print(add_contact(args, book))
            case "add-address":
                print(add_address(args, book))
            case "add-email":
                print(add_email(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "find-contact":
                print(find_contact(args, book))
            case "show-all":
                show_all(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "show-all-birthdays":
                print(show_birthdays_within_days(args, book))
            case "birthdays":
                birthdays(book)
            case "add-note":
                print(add_note(args, note_book))
            case "edit-note-content":
                print(edit_note_content(args, note_book))
            case "delete-note":
                print(delete_note(args, note_book))
            case "show-note":
                print(show_note_by_name(args, note_book))
            case "show-all-notes":
                print(show_all_notes_sorted_by_name(note_book))
            case "show-notes-tag":
                print(show_notes_by_tag(args, note_book))
            case "show-all-notes-tag":
                print(show_all_notes_sorted_by_tag(note_book))
            case _ if command in commands_to_close:
                save_users(book.export(), filename="users_data.json")
                save_notes(note_book.export(), filename="notes_data.json")
                print(Fore.GREEN + "Good bye! 😊")
                break
            case _:
                print(
                    Fore.RED + "⚠️ Invalid command. Please type 'help' for assistance. ⚠️"
                )


if __name__ == "__main__":
    main()
