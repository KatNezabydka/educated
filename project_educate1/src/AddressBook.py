from collections import UserDict
from datetime import datetime, timedelta

from project_educate1.src.Record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def delete(self, name: str) -> None:
        del self.data[name]

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def export(self) -> list:
        existing_data = []
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
