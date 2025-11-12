import re
def get_email():
    while True:
        email = input("Enter email: ")
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return email
        else:
            print("Invalid email, please try again.")

def get_password():
    while True:
        password = input("Enter password: ")
        # minimum 8 characters long
        # letters, numbers, $%#@
        if re.fullmatch(r"[a-zA-Z0-9@\$#%]{8,}", password):
            return password
        else:
            print("Invalid password, please try again.")

if __name__ == "__main__":
    email = get_email()
    password = get_password()
    print(f"your login details are as follows:{email} @ {password}")

