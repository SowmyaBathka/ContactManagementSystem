from data_store import contacts
from validations import validate_name,validate_phone,validate_email
from storage import save_contacts

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

    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists.")
            return
        
    contacts.append(contact)
    save_contacts(contacts)

    print("Contact Added Successfully!!!")

def view_contacts():
    print("\n---View Contacts---")

    if len(contacts)==0:
        print("No Contacts Available.")
        return

    for index,contact in enumerate(contacts,start=1):
        print(f"\nContact: {index}")
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

            print("\nCurrent Contact Details:")
            print("--------------------")
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

            save_contacts(contacts)

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
            confirm=input(f"Are You sure you want to delete {contact['name']}?(Yes/No):")

            if confirm.strip().lower()=="yes":
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!!!")
            else:
                print("Deletion cancelled.")

            return 
    print("Contact not found.")


def search_contact():
    print("\n---Search Contact---")

    if len(contacts)==0:
        print("No Contacts Available.")
        return
    
    search_value=input("Enter name or phone number to search:").strip()

    found_contacts=[]

    for contact in contacts:
        if(
            contact["name"].lower()==search_value.lower()
            or contact["phone"]== search_value
        ):
            found_contacts.append(contact)
        
    if len(found_contacts)==0:
        print("Contact Not Found.")
        return 
        
    print("\nMatching Contacts:")

    for contact in found_contacts:
        print("-----------------")
        print("\nContact Found:")
        print("Name:",contact["name"])
        print("Phone:",contact["phone"])
        print("Email:",contact["email"])