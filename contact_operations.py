from data_store import contacts

def add_contacts():
    print("\n---Add New Contact---")

    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email Address: ")

    contact={
        "name":name,
        "phone":phone,
        "email":email
    }

    contacts.append(contact)

    print("Contact Added Successfully!!!")

def view_contacts():
    print("\nView Contact feature will be implemented later.")

def update_contact():
    print("\nUpdate Contact feature will be implemented later.")

def delete_contact():
    print("\nDelete Contact feature will be implemented later.")