from faker import Faker
import json
import re

fake = Faker()


def generate_fake_user():

    try:
        return {
            "name": fake.first_name(),
            "birthday": fake.date_of_birth().strftime("%d.%m.%Y"),
            "phone": re.sub(r"\D", "", fake.phone_number())[:10],
            "email": fake.email(),
            "address": fake.address(),
        }
    except Exception as e:
        print(f"Error generating fake user: {e}")
        return []


def generate_fake_users(count=10):
    return [generate_fake_user() for _ in range(count)]


def load_users() -> list:

    users_data = generate_fake_users()

    return users_data


def save_users(users_data, filename="users_data.json"):
    try:
        with open(filename, "w") as file:
            json.dump(users_data, file, indent=4)
        print("Users data saved successfully.")
    except Exception as e:
        print(f"Error saving users data: {e}")


def load_or_generate_users():
    try:
        with open("users_data.json", "r") as file:
            print(f"!!! Loading users from the file: users_data.json !!!")
            users_data = json.load(file)
    except FileNotFoundError:
        print("No existing user data file found. Generating fake users...")
        users_data = generate_fake_users()
        save_users(users_data)
    except Exception as e:
        print(f"Error loading users from file: {e}")
        users_data = []
    return users_data
