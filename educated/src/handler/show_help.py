from colorama import Style, Fore


def show_help():
    """
    Print available commands with color highlighting
    """
    print("*" * 30 + " < HELP MENU START > " + "*" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "Available commands:")
    print(Fore.YELLOW + "--> hello: Get a greeting from the bot.")
    print("")
    print(
        Fore.YELLOW
        + "--> add-contact [name] [phone]: Add a new contact with the name and phone number."
    )
    print(
        Fore.YELLOW
        + "--> add-birthday [name] [birthday]: Add a birthday for the specified contact."
    )
    print(
        Fore.YELLOW
        + "--> add-email [name] [email]: Add an email address for the specified contact."
    )
    print(
        Fore.YELLOW
        + "--> add-address [name] [address]: Add an address for the specified contact."
    )
    print(
        Fore.YELLOW
        + "--> show-phone [name]: Show the phone number for the specified contact."
    )
    print(
        Fore.YELLOW
        + "--> edit-phone [name] [new phone]: Change the phone number for the specified contact."
    )
    print(
        Fore.YELLOW
        + "--> show-birthday [name]: Show the birthday for the specified contact."
    )
    print(Fore.YELLOW + "--> find-contact: [name] show all information about person")
    print(Fore.YELLOW + "--> show-contacts: Show all contacts in the address book.")
    print("")
    print(
        Fore.YELLOW
        + "--> show-birthdays [days]: Show birthdays happening within the specified number of days."
    )
    print(
        Fore.YELLOW
        + "--> birthdays-next-week: Show birthdays happening within the next week."
    )
    print("")
    print(
        Fore.YELLOW
        + "--> add-note [note] [tag] [content]: Add a note to the note book."
    )
    print(
        Fore.YELLOW
        + "--> edit-note-content [note_name] [new_content]: Edit the content of a note."
    )
    print(Fore.YELLOW + "--> edit-note-tag [note_name] [new_tag]: Edit the note tag.")
    print(
        Fore.YELLOW + "--> delete-note [note_name]: Delete a note from the note book."
    )
    print(
        Fore.YELLOW + "--> show-note [note_name]: Show the content of a note by its ID."
    )
    print(
        Fore.YELLOW
        + "--> show-all-notes: Show all notes in the note book, sorted by name."
    )
    print(
        Fore.YELLOW + "--> find-notes-by-tag [tag]: Show notes in the note book by tag."
    )
    print(
        Fore.YELLOW
        + "--> show-all-notes-tag: Show all notes in the note book, sorted by tag."
    )
    print("")
    print(Fore.RED + "--> close or exit: Close the program.")
    print("*" * 30 + " < HELP MENU END > " + "*" * 30)
    print(Style.RESET_ALL)  # Reset colors
