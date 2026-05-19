from contact_operations import (
    add_contacts,
    view_contacts,
    update_contact,
    delete_contact
)


def show_menu():
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contacts()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("\nExiting Contact Management System...")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


main()