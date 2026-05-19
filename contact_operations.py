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
    print("\n---Conatcts List---")

    if len(contacts)==0:
        print("No Contacts Found.")

    for contact in contacts:
        print("-----------------")
        print("Name:",contact["name"])
        print("Phone:",contact["phone"])
        print("Email:",contact["email"])

def update_contact():
    print("\n---Update Contact---")

    if len(contacts)==0:
        print("No Contacts available to update.")
        return
    view_contacts()

    contact_name=input("\nEnter the name of the contact to update:")

    for contact in contacts:
        if contact["name"].lower()==contact_name.lower():
            new_phone=input("Enter new phone number:")
            new_email=input("Enter new email address:")

            contact["phone"]=new_phone
            contact["email"]=new_email

            print("Contact updated successfully!!")
            return 
        
    print("Contact not found.")

def delete_contact():
    print("\nDelete Contact feature will be implemented later.")