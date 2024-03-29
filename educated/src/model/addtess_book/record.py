from educated.src.model.contact.address import Address
from educated.src.model.contact.email import Email
from educated.src.model.contact.name import Name
from educated.src.model.contact.phone import Phone
from educated.src.model.contact.birthday import Birthday


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.addresses = []
        self.birthday = birthday

        if birthday is not None:
            self.birthday = Birthday(birthday)

    def add_phone(self, phone) -> "Record":
        self.phones.append(Phone(phone))

        return self

    def add_email(self, email) -> "Record":
        self.emails.append(Email(email))

        return self

    def has_email(self) -> bool:
        return len(self.emails) > 0

    def add_address(self, address) -> "Record":
        self.addresses.append(Address(address))

        return self

    def has_address(self) -> bool:
        return len(self.addresses) > 0

    def delete_phones(self) -> "Record":
        self.phones = []
        return self

    def delete_emails(self) -> "Record":
        self.emails = []
        return self

    def delete_addresses(self) -> "Record":
        self.emails = []
        return self

    def delete_phone(self, phone_for_delete):
        self.phones = [
            phone for phone in self.phones if phone.value != phone_for_delete
        ]

    def delete_email(self, email_for_delete):
        self.emails = [
            email for email in self.emails if email.value != email_for_delete
        ]

    def delete_address(self, address_for_delete):
        self.emails = [
            address for address in self.addresses if address.value != address_for_delete
        ]

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.add_phone(new_phone)

    def edit_email(self, old_email, new_email):
        self.delete_email(old_email)
        self.add_email(new_email)

    def edit_address(self, new_address):
        self.delete_addresses()
        self.add_address(new_address)

    def find_phone(self, search_phone):
        for phone in self.phones:
            if phone.value == search_phone:
                return phone.value
        return None

    def print_phones(self) -> str:
        return f"📞 phones: {'; '.join(phone.value for phone in self.phones)}"

    def print_emails(self) -> str:
        if not self.emails:
            return ""
        else:
            return f"📧 email: {'; '.join(email.value for email in self.emails)}"

    def print_addresses(self) -> str:
        if not self.addresses:
            return ""
        else:
            return f"🏘 addres: {'; '.join(address.value for address in self.addresses)}"

    def print_birthday(self) -> str:
        if self.has_birthday():
            return f"🎂 birthday: {self.birthday.value.strftime('%d.%m.%Y')}"
        return ""

    def add_birthday(self, birthday) -> "Record":
        self.birthday = Birthday(birthday)
        return self

    def get_birthday(self) -> Birthday:
        return self.birthday

    def has_birthday(self) -> bool:
        return self.birthday is not None

    def __str__(self):
        return f"Contact name: {self.name.value}, {self.print_birthday()} {self.print_phones()} {self.print_addresses()} {self.print_emails()}"
