from educated.src.handler.input_error import input_error
from educated.src.model.note.note_book import NoteBook
from educated.src.model.validation.validation_error import ValidationError


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
        This handler deletes a note from the notebook based on its name.
    """
    if len(args) == 0:
        raise ValidationError("Name cannot be empty.")
    name = args[0]

    note_book.delete_note(name)
    return "✅ Note deleted."
