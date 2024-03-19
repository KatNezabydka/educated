from __future__ import annotations

from colorama import init, Fore, Style, Back
from prompt_toolkit import prompt

from educated.src.handler.add_address import add_address
from educated.src.handler.add_birthday import add_birthday
from educated.src.handler.add_contact import add_contact
from educated.src.handler.add_email import add_email
from educated.src.handler.add_note import add_note
from educated.src.handler.birthdays import birthdays
from educated.src.handler.change_contact import change_contact
from educated.src.handler.delete_note import delete_note
from educated.src.handler.edit_note_content import edit_note_content
from educated.src.handler.edit_note_tag import edit_note_tag
from educated.src.handler.find_contact import find_contact
from educated.src.handler.parse_input import parse_input
from educated.src.handler.show_all import show_all
from educated.src.handler.show_birthday import show_birthday
from educated.src.handler.show_birthdays_within_days import show_birthdays_within_days
from educated.src.handler.show_help import show_help
from educated.src.handler.show_note_by_name import show_note_by_name
from educated.src.handler.show_notes_by_tag import show_notes_by_tag
from educated.src.handler.show_phone import show_phone
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.note.note_book import NoteBook
from educated.src.utils.faker.user_management import load_or_generate_users, save_users
from educated.src.utils.faker.note_management import load_or_generate_notes, save_notes
from educated.src.utils.custom_completer.custom_completer import (
    CustomCompleter,
    custom_style,
)
from educated.src.model.note.note import Note
from educated.src.model.addtess_book.record import Record

completer = CustomCompleter()


def prompt_with_completion():
    text = prompt("Enter a command: ", style=custom_style, completer=completer)
    return text


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
        if "email" in user and user["email"] is not None:
            fake_user.add_email(user["email"])
        if "address" in user and user["address"] is not None:
            fake_user.add_address(user["address"])
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
            case "add-contact":
                print(add_contact(args, book))
            case "add-address":
                print(add_address(args, book))
            case "add-email":
                print(add_email(args, book))
            case "edit-phone":
                print(change_contact(args, book))
            case "show-phone":
                print(show_phone(args, book))
            case "find-contact":
                print(find_contact(args, book))
            case "show-contacts":
                show_all(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "show-birthdays":
                print(show_birthdays_within_days(args, book))
            case "show-next-week-birthdays":
                birthdays(book)
            case "add-note":
                print(add_note(args, note_book))
            case "edit-note-content":
                print(edit_note_content(args, note_book))
            case "edit-note-tag":
                print(edit_note_tag(args, note_book))
            case "delete-note":
                print(delete_note(args, note_book))
            case "show-note":
                print(show_note_by_name(args, note_book))
            case "show-all-notes":
                print(note_book.show_all_sorted_by_name())
            case "find-notes-by-tag":
                print(show_notes_by_tag(args, note_book))
            case "show-all-notes-tag":
                print(note_book.show_all_sorted_by_tag())
            case _ if command in commands_to_close:
                save_users(book.export(), filename="users_data.json")
                save_notes(note_book.export(), filename="notes_data.json")
                print(Fore.GREEN + "Good bye! 😊")
                break
            case _:
                print(
                    Fore.RED + "⚠️ Invalid command. Please type 'help' for assistance. ⚠️"
                )
