from collections import UserDict
from Note import Note
from ValidationError import ValidationError


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            raise ValidationError("Give name, tag and content please.")
        except KeyError:
            raise ValidationError("Note not found.")
        except IndexError:
            raise ValidationError("Give name, tag and content please.")
    return wrapper


class NoteBook(UserDict):
    @validate
    def add_note(self, args):
        name = args[0]
        tag = args[1]
        content = " ".join(args[2:])
        self.data[name] = Note(name, tag, content)

    @validate
    def edit_note_content(self, name, new_content):
        self.data[name].content = new_content

    @validate
    def edit_note_tag(self, name, new_tag):
        self.data[name].tag = new_tag

    @validate
    def delete_note(self, name):
        del self.data[name]

    @validate
    def show_by_name(self, name):
        return str(self.data[name])

    def show_all_sorted_by_name(self):
        sorted_notes = sorted(self.data.items(), key=lambda x: x[0])
        if len(sorted_notes) == 0:
            return "No notes have been found"
        return "\n\n".join([str(note) for name, note in sorted_notes])

    def show_by_tag(self, tag):
        notes_with_tag = [str(note) for note in self.data.values() if note.tag == tag]
        if notes_with_tag:
            return "\n\n".join(notes_with_tag)
        else:
            return "No notes have been found with this tag."

    def show_all_sorted_by_tag(self):
        sorted_notes = sorted(self.data.items(), key=lambda x: x[1].tag)
        if len(sorted_notes) == 0:
            return "No notes have been found"
        return "\n\n".join([str(note) for name, note in sorted_notes])
