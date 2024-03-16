from datetime import datetime

from educated.src.Field import Field
from educated.src.ValidationError import ValidationError


def validate_birthday(func):
    def wrapper(*args, **kwargs):
        value = args[1]
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except Exception:
            raise ValidationError("Incorrect date format. Use DD.MM.YYYY.")
        return func(*args, **kwargs)

    return wrapper


class Birthday(Field):
    @validate_birthday
    def __init__(self, value):
        super().__init__(datetime.strptime(value, "%d.%m.%Y"))
