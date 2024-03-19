from educated.src.handler.input_error import input_error
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler retrieves and returns the notes from the notebook based on their tag.
    """
    if len(args) == 0:
        raise ValidationError("Tag cannot be empty.")
    tag = args[0]
    return note_book.show_by_tag(tag)
