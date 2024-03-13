from Field import Field


class Name(Field):
    def __init__(self, value: str):
        if not value.isalpha():
            print("The name must consist letters only")
            raise ValueError
        if not value.istitle():
            print("The name must start with an upper case letter and the rest letter must be lower case")
            raise ValueError
        self.value = value
