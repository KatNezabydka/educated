from Field import Field
from ValidationError import ValidationError



def validate_name(func):
    def wrapper(value):
        if not value.isalpha():
            print("The name must consist of letters only")
            raise ValidationError("The name must consist of letters only")
        if not value.istitle():
            print("The name must start with an upper case letter and the rest letters must be lower case")
            raise ValidationError("The name must start with an upper case letter and the rest letters must be lower case")
        return func
    return wrapper
        
class Name(Field):
    @validate_name
    def __init__(self, value):
        super().__init__(value)
