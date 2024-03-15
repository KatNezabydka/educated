from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style as StylePrompt

custom_style = StylePrompt.from_dict(
    {
        "prompt": "#ansiblue",
        "prompt_separator": "#ansiblue bold",
        "completion-menu.completion": "bg:#ansiyellow #ansiblack",
        "completion-menu.completion.current": "bg:#ansiblue #ansiwhite",
    }
)


class CustomCompleter(Completer):
    def __init__(self):
        self.completions = [
            "help",
            "hello",
            "add",
            "add-address",
            "add-email",
            "change",
            "phone",
            "find-contact",
            "show-all",
            "add-birthday",
            "show-birthday",
            "birthdays",
            "add-note",
            "edit-note-content",
            "delete-note",
            "show-note",
            "show-all-birthdays",
            "show-all-notes",
            "show-notes-tag",
            "show-all-notes-tag",
            "exit",
            "close"
        ]

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        for completion in self.completions:
            if completion.startswith(text_before_cursor):
                yield Completion(completion, start_position=-len(text_before_cursor))
