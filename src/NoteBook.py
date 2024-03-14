from collections import UserDict
from Note import Note
from ValidationError import ValidationError


class NoteBook(UserDict):
    def add_note(self, name, tag, content):
        try:
            self.data[name] = Note(name, tag, content)
        except ValidationError:
            print("Error: Note validation failed.")

    def edit_note_content(self, name, new_content):
        try:
            self.data[name].content = new_content
        except ValidationError:
            raise ValidationError("Note validation failed.")

    def edit_note_tag(self, name, new_tag):
        try:
            self.data[name].tag = new_tag
        except ValidationError:
            raise ValidationError("Note validation failed.")

    def delete_note(self, name):
        try:
            del self.data[name]
        except ValidationError:
            raise ValidationError("Note validation failed.")

    def show_by_name(self, name):
        try:
            return str(self.data[name])
        except ValidationError:
            raise ValidationError("Note validation failed.")

    def show_all_sorted_by_name(self):
        try:
            sorted_notes = sorted(self.data.items(), key=lambda x: x[0])
            return '\n\n'.join([str(note) for name, note in sorted_notes])
        except ValidationError:
            return "Note validation failed."

    def show_by_tag(self, tag):
        try:
            notes_with_tag = [str(note) for note in self.data.values() if note.tag == tag]
            if notes_with_tag:
                return '\n\n'.join(notes_with_tag)
            else:
                return "No notes found with this tag."
        except ValidationError:
            return "Note validation failed."

    def show_all_sorted_by_tag(self):
        try:
            sorted_notes = sorted(self.data.items(), key=lambda x: x[1].tag)
            return '\n\n'.join([str(note) for name, note in sorted_notes])
        except ValidationError:
            return "Note validation failed."

