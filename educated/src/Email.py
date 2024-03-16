import re

from educated.src.Field import Field
from educated.src.ValidationError import ValidationError


def validate_email(func):
    def wrapper(*args, **kwargs):
        email = args[1]
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValidationError(
                "Incorrect email, please use a valid email format (e.g., example@example.com)"
            )
        return func(*args, **kwargs)

    return wrapper


class Email(Field):
    @validate_email
    def __init__(self, value):
        super().__init__(value)
