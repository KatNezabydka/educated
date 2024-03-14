from Address import Address
from Name import Name
from Birthday import Birthday
from Phone import Phone
from Email import Email


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

        if birthday is not None:
            self.birthday = Birthday(birthday)

    def add_phone(self, phone) -> "Record":
        self.phones.append(Phone(phone))

        return self

    def delete_phones(self) -> "Record":
        self.phones = []
        return self

    def delete_phone(self, phone_for_delete):
        self.phones = [
            phone for phone in self.phones if phone.value != phone_for_delete
        ]

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, search_phone):
        for phone in self.phones:
            if phone.value == search_phone:
                return phone.value
        return None

    def print_phones(self) -> str:
        return f"phones: {'; '.join(phone.value for phone in self.phones)}"

    def add_birthday(self, birthday) -> "Record":
        self.birthday = Birthday(birthday)
        return self

    def show_birthday(self):
        print(self.birthday.value.strftime("%d.%m.%Y"))

    def has_birthday(self) -> bool:
        return self.birthday != None

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday} phones: {'; '.join(phone.value for phone in self.phones)}"



