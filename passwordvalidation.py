valid_password = False

while not valid_password:
    password = input("Enter a password (must be at least 6 characters long): ")
    if len(password) > 5:
        valid_password = True
        print("Password accepted.")
    else:
        print("Invalid password. Please enter a password with at least 6 characters.")
