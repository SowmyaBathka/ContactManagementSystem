def validate_name(name):
    if name.strip()=="":
        print("Name cannot be empty.")
        return False
    return True
def validate_phone(phone):
    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return False
    if len(phone)!=10:
        print("Phone number must be exactly 10 digits.")
        return False
    return True

def validate_email(email):
    if "@" not in email or "." not in email:
        print("Enter a Valid email address.")
        return False
    return True