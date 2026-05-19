from data_store import contacts
from validations import validate_name,validate_phone,validate_email

def add_contacts():
    print("\n---Add New Contact---")

    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email Address: ")

    if not validate_name(name):
        return 
    
    if not validate_phone(phone):
        return 
    
    if not validate_email(email):
        return
    

    contact={
        "name":name,
        "phone":phone,
        "email":email
    }

    contacts.append(contact)

    print("Contact Added Successfully!!!")

def view_contacts():
    print("\n---Contacts List---")

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

            print("\nCurrent Details:")
            print("Name:",contact["name"])
            print("Phone:",contact["phone"])
            print("Email:",contact["email"])

            new_phone=input("Enter new phone number(Press Enter to Keep current):")
            new_email=input("Enter new email address(Press Enter to Keep current):")

            if new_phone!="":
                if not validate_phone(new_phone):
                    return
                contact["phone"]=new_phone
            
            if new_email!="":
                if not validate_email(new_email):
                    return
                contact["email"]=new_email

            print("Contact updated successfully!!")
            return 
        
    print("Contact not found.")

def delete_contact():
    print("\n---Delete Contact---")

    if len(contacts)==0:
        print("No Conatcts available to delete.")
        return
    
    view_contacts()

    contact_name=input("\nEnter the name of the contact to delete:")

    for contact in contacts:
        if contact["name"].lower()==contact_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!!!")
            return 
    print("Contact not found.")
