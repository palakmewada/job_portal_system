def check_name(name):
    if name=="":
        return False
    else:
        return True

    
def check_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


def check_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False


def check_choice(choice, minimum, maximum):
    if choice.isdigit():
        number=int(choice)


        if minimum <= number <= maximum:
            return True
        else:
            return False
    else:
        return False