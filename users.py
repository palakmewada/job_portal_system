from file_manager import save_data, read_data
from validation import check_name, check_email, check_phone

def register_user():
    print("\n=== USER REGISTRATION ===")
    name = input("Enter your name:")

    if check_name(name) == False:
        print("Name cannot be empty.")
        return
    
    email = input("Enter your email: ")

    if check_email(email) == False:
        print("Please enter a valid email.")
        return

    phone = input("Enter your phone number: ")

    if check_phone(phone) == False:
        print("Please enter a valid 10-digit phone number.")
        return

    user = name + "," + email + "," + phone

    save_data("data/users.txt", user)

    print("\nUser registered successfully!")
    print("Name  :", name)
    print("Email :", email)
    print("Phone :", phone)
    print("=======================================")


def view_users():
    print("\n=== REGISTERED USERS ===")

    users = read_data("data/users.txt")

    if len(users) == 0:
        print("No users are registered yet.")
    else:
        for user in users:
            user = user.strip()
            details = user.split(",")

            print("\nName  :", details[0])
            print("Email :", details[1])
            print("Phone :", details[2])

    print("===")



