
from AddressBook import AddressBook
from Record import Record
from ValidationError import ValidationError

ERROR_MESSAGES = {
    ValueError: "Give me name and phone/birthday please.",
    ValidationError: lambda e: str(e),
    KeyError: "Contact not found.",
    AttributeError: "Contact not found.",
    IndexError: "Give me name."
}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = ERROR_MESSAGES.get(type(e))
            if error_message:
                if callable(error_message):
                    return error_message(e)
                else:
                    return error_message
            else:
                raise e
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, book: AddressBook) -> str:
    name, phone = args
    if book.find(name) == None:
        book.add_record(Record(name).add_phone(phone))
        return "Contact added."
    return "Contact already exist."

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, phone = args
    contact = book.find(name)
    if  contact != None:
        contact.delete_phones().add_phone(phone)
        return "Contact updated."
    return "Contact not found."
    

@input_error
def show_phone(args: list, book: AddressBook) -> str:
    name = args[0]
    return book.find(name).print_phones()
    
def show_all(book: AddressBook) -> print:
    if len(book.data) == 0:
        print("The list is empty")
    for name, record in book.data.items():
        print(f"{name}. {record.print_phones()}")
  
@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)
    if record != None and record.has_birthday() == False:
        record.add_birthday(birthday)
        return "Birthday added."
    return "Contact not found or birthday already exist."  

@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record != None and record.has_birthday() != False:
        return record.show_birthday()
    return "Contact not found or birthday is empty"  

def birthdays(book: AddressBook) -> print:
    if len(book.data) == 0:
        print("The list is empty")
    for day, names in book.get_birthdays_per_week().items():
        if names:
            print(f"{day}: {', '.join(names)}")

def main():
    book = AddressBook()
    commands_to_close = ["close", "exit"]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        match command:
            case "hello":
                 print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "show_all":
                show_all(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                birthdays(book)
            case _ if command in commands_to_close:
                print("Good bye!")
                break
            case _:
                 print("Invalid command.")

if __name__ == "__main__":
    main()