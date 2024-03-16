# project-educate1

Console bot assistant

### Prerequisites

- Python (version 3.X.X)
- Git (version 2.X.X)

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/KatNezabydka/project-educate1.git
   ```

2. Install the package:

   ```bash
   pip install .
   ```

3. Run from console:

   ```bash
   educate
   ```

### Additional Setup

- Ensure Python is installed on your system. If not, download and install Python from the [official website](https://www.python.org/).
- Set up Git on your local machine if you haven't already. Download and install Git from the [official website](https://git-scm.com/).

## Libraries Used

- **[Black](https://github.com/psf/black)**: A Python code formatter.
- **[Colorama](https://github.com/tartley/colorama)**: Cross-platform colored terminal text.
- **[Faker](https://github.com/joke2k/faker)**: Fake data generator for Python.
- **[Prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)**: Interactive command line

# Chat Bot

### Introduction

This chat bot provides functionality to manage an address book. It offers the following commands:

- `help`: Calls the `show_help()` function, which displays usage help for the program.
- `hello`: Prints a greeting message.
- `add [name] [phone]`: Adds a new contact with the specified name and phone number.
- `add-address [name] [address]`: Adds an address for the specified contact.
- add-email [name] [email]`: Adds an email address for the specified contact.
- `change [name] [new phone]`: Changes the phone number for the specified contact.
- `phone [name]`: Shows the phone number for the specified contact.
- `find-contact: [name]` show all information about person
- `show_all`: Shows all contacts in the address book.
- `add-birthday [name] [birthday]`: Adds a birthday for the specified contact.
- `show-birthday [name]`: Shows the birthday for the specified contact.
- `birthdays`: Shows birthdays happening within the next week.
- `add-note [note]`: Adds a new note to the notebook.
- `edit-note-content [note_id] [new_content]`: Edits the content of the note with the specified ID.
- `delete-note [note_id]`: Deletes the note with the specified ID.
- `show-note [note_id]`: Shows the note with the specified ID.
- `show-all-notes`: Shows all notes, sorted by name.
- `show-notes-tag [tag]`: Shows notes with the specified tag.
- `show-all-notes-tag`: Shows all notes, sorted by tags.
- `close` or `exit`: Closes the program, saving data before exiting.

The chat bot supports color highlighting for commands and error messages for user convenience.

## Authors

- [KatNezabydka](https://github.com/KatNezabydka) - Team Lead / Python developer
- [eilerbit](https://github.com/eilerbit) - Scrum master / Python developer
- [Maria-Shymanska](https://github.com/Maria-Shymanska) - Python developer
- [serhiizghama](https://github.com/serhiizghama) - Python developer
- [Ingoo1](https://github.com/Ingoo1) - Python developer

## License

This project is licensed under the [MIT License](https://github.com/KatNezabydka/project-educate1).
