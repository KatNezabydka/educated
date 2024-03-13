from Name import Name
from Birthday import Birthday
from Phone import Phone


# class Record:
#     def __init__(self, name, birthday=None):
#         self.name = Name(name)
#         self.phones = []
#         self.birthday = birthday

#         if birthday is not None:
#             self.birthday = Birthday(birthday)

#     def add_phone(self, phone) -> "Record":
#         self.phones.append(Phone(phone))

#         return self

#     def delete_phones(self) -> "Record":
#         self.phones = []
#         return self

#     def delete_phone(self, phone_for_delete):
#         self.phones = [
#             phone for phone in self.phones if phone.value != phone_for_delete
#         ]

#     def edit_phone(self, old_phone, new_phone):
#         self.delete_phone(old_phone)
#         self.add_phone(new_phone)

#     def find_phone(self, search_phone):
#         for phone in self.phones:
#             if phone.value == search_phone:
#                 return phone.value
#         return None

#     def print_phones(self) -> str:
#         return f"phones: {'; '.join(phone.value for phone in self.phones)}"

#     def add_birthday(self, birthday) -> "Record":
#         self.birthday = Birthday(birthday)
#         return self

#     def show_birthday(self):
#         print(self.birthday.value.strftime("%d.%m.%Y"))

#     def has_birthday(self) -> bool:
#         return self.birthday != None

#     def __str__(self):
#         return f"Contact name: {self.name.value}, birthday: {self.birthday} phones: {'; '.join(phone.value for phone in self.phones)}"



class Record:
    def __init__(self, name, birthday=None):
        try:
            self.name = Name(name)
        except Exception as e:
            print(f"Error creating name: {e}")
            self.name = None

        self.phones = []
        self.birthday = birthday

        if birthday is not None:
            try:
                self.birthday = Birthday(birthday)
            except Exception as e:
                print(f"Error creating birthday: {e}")

    def add_phone(self, phone) -> "Record":
        try:
            self.phones.append(Phone(phone))
        except Exception as e:
            print(f"Error adding phone: {e}")

        return self

    def delete_phones(self) -> "Record":
        try:
            self.phones = []
        except Exception as e:
            print(f"Error deleting phones: {e}")
        return self

    def delete_phone(self, phone_for_delete):
        try:
            self.phones = [
                phone for phone in self.phones if phone.value != phone_for_delete
            ]
        except Exception as e:
            print(f"Error deleting phone: {e}")

    def edit_phone(self, old_phone, new_phone):
        try:
            self.delete_phone(old_phone)
            self.add_phone(new_phone)
        except Exception as e:
            print(f"Error editing phone: {e}")

    def find_phone(self, search_phone):
        try:
            for phone in self.phones:
                if phone.value == search_phone:
                    return phone.value
        except Exception as e:
            print(f"Error finding phone: {e}")
        return None

    def print_phones(self) -> str:
        try:
            return f"phones: {'; '.join(phone.value for phone in self.phones)}"
        except Exception as e:
            print(f"Error printing phones: {e}")
            return "Error printing phones"

    def add_birthday(self, birthday) -> "Record":
        try:
            self.birthday = Birthday(birthday)
        except Exception as e:
            print(f"Error adding birthday: {e}")
        return self

    def show_birthday(self):
        try:
            print(self.birthday.value.strftime("%d.%m.%Y"))
        except Exception as e:
            print(f"Error showing birthday: {e}")

    def has_birthday(self) -> bool:
        try:
            return self.birthday is not None
        except Exception as e:
            print(f"Error checking birthday: {e}")
            return False

    def __str__(self):
        try:
            return f"Contact name: {self.name.value}, birthday: {self.birthday} phones: {'; '.join(phone.value for phone in self.phones)}"
        except Exception as e:
            print(f"Error converting to string: {e}")
            return "Error converting to string"
