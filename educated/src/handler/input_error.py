from colorama import Fore

from educated.src.model.validation.validation_error import ValidationError


def input_error(func):
    """
    Decorator to handle input errors gracefully.

    This decorator catches exceptions that occur within the decorated handler.
    If an exception occurs, it looks up an appropriate error message based on the type of the exception
    and returns it. If no specific error message is found, it re-raises the exception.

    Parameters:
        func: The handler to be decorated.

    Returns:
        The decorated handler.

    Notes:
        This decorator is useful for handling errors that may occur due to invalid input.
        It provides a way to customize error messages for specific exception types.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return Fore.RED + str(e)
        except Exception as e:
            if not callable(e):
                return Fore.RED + str(e)
            else:
                raise e

    return inner
