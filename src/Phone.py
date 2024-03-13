from Field import Field
from ValidationError import ValidationError


def validate_phone(func):
    def wrapper(*args, **kwargs):
        value = args[1]
        if not value.isdigit() or len(value) != 10:
            raise ValidationError("Incorrect phone format")
        return func(*args, **kwargs)

    return wrapper


class Phone(Field):
    @validate_phone
    def __init__(self, value):
        super().__init__(value)
