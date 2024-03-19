from educated.src.handler.input_error import input_error
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler retrieves and returns the content of a note from the notebook based on its name.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]
    return note_book.show_by_name(name)
