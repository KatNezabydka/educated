from faker import Faker
import json


fake = Faker()


def generate_fake_note():
    try:
        return {
            "name": fake.word().capitalize(),
            "tag": fake.word().lower(),
            "content": fake.text(max_nb_chars=300)
        }
    except Exception as e:
        print(f"Error generating fake note: {e}")
        return None


def generate_fake_notes(count=10):
    return [generate_fake_note() for _ in range(count)]


def load_notes() -> list:
    try:
        with open("notes_data.json", "r") as file:
            print(f"!!! Loading notes from the file: notes_data.json !!!")
            notes_data = json.load(file)
    except FileNotFoundError:
        print("No existing note data file found. Generating fake notes...")
        notes_data = generate_fake_notes()
        save_notes(notes_data)
    except Exception as e:
        print(f"Error loading notes from file: {e}")
        notes_data = []
    return notes_data


def save_notes(notes_data, filename="notes_data.json"):
    try:
        with open(filename, "w") as file:
            # Serialize note objects to JSON
            json.dump(notes_data, file, indent=4)
        print("Notes data saved successfully.")
    except Exception as e:
        print(f"Error saving notes data: {e}")


def load_or_generate_notes():
    return load_notes()
