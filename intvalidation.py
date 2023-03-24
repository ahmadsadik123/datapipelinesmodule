valid_input = False

while not valid_input:
    user_input = input("Enter an integer: ")
    if user_input.isdigit():
        valid_input = True
        integer_input = int(user_input)
    else:
        print("Invalid input. Please enter an integer.")

print("The input value is:", integer_input)
