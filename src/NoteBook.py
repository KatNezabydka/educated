from collections import UserDict
from Note import Note


class NoteBook(UserDict):
    def add_note(self, name, tag, content):
        self.data[name] = Note(name, tag, content)

    def edit_note_content(self, name, new_content):
        if name in self.data:
            self.data[name].content = new_content
        else:
            raise KeyError("Note not found.")

    def edit_note_tag(self, name, new_tag):
        if name in self.data:
            self.data[name].tag = new_tag
        else:
            raise KeyError("Note not found.")

    def delete_note(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Note not found.")

    def show_by_name(self, name):
        if name in self.data:
            return str(self.data[name])
        else:
            raise KeyError("Note not found.")

    def show_all_sorted_by_name(self):
        sorted_notes = sorted(self.data.items(), key=lambda x: x[0])
        return '\n\n'.join([str(note) for name, note in sorted_notes])
