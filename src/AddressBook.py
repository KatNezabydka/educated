from Record import Record

from collections import UserDict
from datetime import datetime, timedelta
from ValidationError import ValidationError


def validate_address_book(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            raise ValidationError("Give me name and phone/birthday please.")
        except KeyError:
            raise ValidationError("Contact not found.")
        except AttributeError:
            raise ValidationError("Contact not found.")
        except IndexError:
            raise ValidationError("Give me name.")
    return wrapper


class AddressBook(UserDict):
    @validate_address_book
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    @validate_address_book
    def delete(self, name: str) -> None:
        del self.data[name]

    @validate_address_book
    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def export(self) -> list:
        existing_data = []
        default_data = datetime.today()
        for record in self.data.values():
            existing_data.append(
                {
                    "name": record.name.value,
                    "phone": record.phones[0].value if record.phones else None,
                    "birthday": (
                        record.birthday.value.strftime("%d.%m.%Y")
                        if record.birthday
                        else None
                    ),
                }
            )
        return existing_data

    def get_birthdays_per_week(self) -> dict:
        today = datetime.now()
        start_day = today + timedelta(days=1)
        end_day = start_day + timedelta(days=7)

        birth_week = {
            day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        }

        for name, record in self.data.items():
            if record.has_birthday():
                contact_birthday = record.birthday.value.replace(year=today.year)

                if (
                    contact_birthday.month == 2
                    and contact_birthday.day == 29
                    and not today.year % 4 == 0
                ):
                    contact_birthday = contact_birthday.replace(day=28)
                if start_day <= contact_birthday < end_day:
                    if (
                        contact_birthday.weekday() == 5
                        or contact_birthday.weekday() == 6
                    ):
                        birth_day = "Monday"
                    else:
                        birth_day = contact_birthday.strftime("%A")
                    birth_week[birth_day].append(name)

        return birth_week
