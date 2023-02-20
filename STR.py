import re

def validate_input(prompt):
    while True:
        user_input = input(prompt)
        if re.match("^[a-zA-Z-!@#$%^&*(),.?\":{}|<>]*$", user_input):
            return user_input
        else:
            print("Invalid input! Please only use letters, numbers, and special characters.")

input_value = validate_input("Enter a value: ")
print("You entered: ", input_value)