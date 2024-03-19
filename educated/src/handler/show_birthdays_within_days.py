from colorama import Fore

from educated.src.handler.input_error import input_error
from educated.src.model.addtess_book.address_book import AddressBook
from educated.src.model.validation.validation_error import ValidationError


@input_error
def show_birthdays_within_days(args, book: AddressBook) -> str:
    """
    Show birthdays of contacts within specified days.

    Parameters:
        args: The number of days to check for upcoming birthdays.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A string containing all the found upcoming birthdays.

    Notes:
        This handler prints the birthdays of contacts that fall within the specified number of days
        from the current date.
    """

    if len(args) == 0:
        raise ValidationError("Number of days must be provided.")

    try:
        days = int(args[0])
    except ValueError:
        raise ValidationError("Number of days must be an integer.")

    today = datetime.now().date()
    end_date = today + timedelta(days=days)

    birthdays_within_days = []
    for name, contact in book.items():
        birthday = contact.get_birthday()

        if birthday:
            today = datetime.now().date()
            birthday_this_year = datetime(
                today.year, birthday.value.month, birthday.value.day
            )
            if birthday_this_year.date() < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year.date() <= end_date:
                days_until_birthday = (birthday_this_year.date() - today).days

                if days_until_birthday == 0:
                    days_until_str = "(today)"
                elif days_until_birthday == 1:
                    days_until_str = "(tomorrow)"
                else:
                    days_until_str = f"(in {days_until_birthday} days)"

                birthdays_within_days.append(
                    f"{Fore.BLUE}📅{birthday_this_year.strftime('%d.%m.%Y')} {days_until_str} - {Fore.GREEN}👤{name}"
                )
    if len(birthdays_within_days) == 0:
        return f"No upcoming birthdays within the {days} days found"
    return "\n".join(birthdays_within_days)
