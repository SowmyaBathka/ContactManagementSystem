import json


def save_contacts(contacts):
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

    except Exception as error:
        print("Error saving contacts:", error)


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Contacts file is corrupted. Starting with empty contact list.")
        return []

    except Exception as error:
        print("Unexpected error while loading contacts:", error)
        return []