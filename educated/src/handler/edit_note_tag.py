from educated.src.handler.input_error import input_error
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler edits the tag of a note identified by its name and updates it with the new tag.
    """

    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    new_tag = None
    if len(args) > 1:
        new_tag = args[1]

    note_book.edit_note_tag(name, new_tag)
    return "✅ Note tag updated."
