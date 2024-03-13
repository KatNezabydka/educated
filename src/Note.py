class Note:
    def __init__(self, name, tag, content):
        self.name = name
        self.tag = tag
        self.content = content

    def __str__(self):
        return f"Name: {self.name}\nTag: {self.tag if self.tag else 'No Tag'}\nContent: {self.content}"
