from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.note.note import Note
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler adds a note to the notebook with the provided name, tag, and content.
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
        return f"{Fore.GREEN}✅ Note added."
    return f"{Fore.RED}Note with the same name already exists."
