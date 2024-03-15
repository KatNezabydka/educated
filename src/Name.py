from Field import Field
from ValidationError import ValidationError


def validate_name(func):
    def wrapper(*args, **kwargs):
        value = args[1]
        if not value.isalpha():
            raise ValidationError("The name must consist of letters only")
        if not value.istitle():
            raise ValidationError(
                "The name must start with an upper case letter and the rest letters must be lower case"
            )
        return func(*args, **kwargs)

    return wrapper


class Name(Field):
    @validate_name
    def __init__(self, value):
        super().__init__(value)
