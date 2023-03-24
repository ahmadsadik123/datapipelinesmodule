valid_input = False

while not valid_input:
    try:
        age = int(input("Enter your age: "))
        if age >= 13 and age <= 19:
            valid_input = True
            print("You are a teenager.")
        else:
            print("You are not a teenager.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
