# project-educate1

Brief description of your project.

## Local Deployment

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.X.X)
- Git (version 2.X.X)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/KatNezabydka/project-educate1.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_project
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - **Mac / Linux:**

        ```bash
        source env/bin/activate
        ```

    - **Windows:**

        ```bash
        .\env\Scripts\activate
        ```
   - Deactivate the virtual environment - **Mac / Linux / Windows:**:

       ```bash
       deactivate
       ```

5. Install required modules:

    ```bash
    pip install -r requirements.txt
    ```

### Additional Setup

- Ensure Python is installed on your system. If not, download and install Python from the [official website](https://www.python.org/).
- Set up Git on your local machine if you haven't already. Download and install Git from the [official website](https://git-scm.com/).

### Running the Application

Use the following command to run the application:

```bash
python __main__.py
```

## Libraries Used

- **[Black](https://github.com/psf/black)**: A Python code formatter.
- **[Colorama](https://github.com/tartley/colorama)**: Cross-platform colored terminal text.
- **[Faker](https://github.com/joke2k/faker)**: Fake data generator for Python.
- **[Prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)**: Building powerful interactive command line applications


# Chat Bot

### Introduction

This chat bot provides functionality to manage an address book. It offers the following commands:

- ``hello``: Get a greeting from the bot.
- ``add [name] [phone]``: Add a new contact with the name and phone number.
- ``change [name] [new phone]``: Change the phone number for the specified contact.
- ``phone [name]``: Show the phone number for the specified contact.
- ``show_all``: Show all contacts in the address book.
- ``add-birthday [name] [birthday]``: Add a birthday for the specified contact.
- ``show-birthday [name]``: Show the birthday for the specified contact.
- ``birthdays``: Show birthdays happening within the next week.
- ``close`` or ``exit``: Close the program.

The chat bot supports color highlighting for commands and error messages for user convenience.


## Authors

- [KatNezabydka](https://github.com/KatNezabydka) - Team Lead / Python developer
- [eilerbit](https://github.com/eilerbit) - Scrum master / Python developer
- [Maria-Shymanska](https://github.com/Maria-Shymanska) - Python developer
- [serhiizghama](https://github.com/serhiizghama) - Python developer
- [Ingoo1](https://github.com/Ingoo1) - Python developer

## License

This project is licensed under the [MIT License](https://github.com/KatNezabydka/project-educate1).