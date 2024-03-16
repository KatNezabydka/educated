from collections import UserDict

from Note import Note
from ValidationError import ValidationError


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.name] = note

    def edit_note_content(self, name, new_content):
        if name in self.data:
            self.data[name].content = new_content
        else:
            raise ValidationError("Note not found.")

    def edit_note_tag(self, name, new_tag):
        if name in self.data:
            self.data[name].tag = new_tag
        else:
            raise ValidationError("Note not found.")

    def delete_note(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValidationError("Note not found.")

    def show_by_name(self, name):
        if name in self.data:
            return str(self.data[name])
        else:
            raise ValidationError("Note not found.")

    def show_all_sorted_by_name(self):
        sorted_notes = sorted(self.data.items(), key=lambda x: x[0])
        if not sorted_notes:
            return "No notes found"
        return "\n\n".join([str(note) for name, note in sorted_notes])

    def show_by_tag(self, tag):
        notes_with_tag = [str(note) for note in self.data.values() if note.tag == tag]
        if notes_with_tag:
            return "\n\n".join(notes_with_tag)
        else:
            return "No notes found with this tag."

    def show_all_sorted_by_tag(self):
        sorted_notes = sorted(self.data.items(), key=lambda x: x[1].tag)
        if not sorted_notes:
            return "No notes found"
        return "\n\n".join([str(note) for name, note in sorted_notes])

    def export(self) -> list:
        existing_data = []
        for note in self.data.values():
            existing_data.append(note.to_dict())
        return existing_data

    def find(self, name: str) -> Note | None:
        return self.data.get(name, None)
