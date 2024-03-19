from educated.src.handler.input_error import input_error
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler edits the content of a note identified by its name and updates it with the new content.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    new_content = " ".join(args[1:])
    note_book.edit_note_content(name, new_content)
    return "✅ Note content updated."
