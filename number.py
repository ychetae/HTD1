def get_int_input():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return user_input

# Using the function
input_value = get_int_input()
print("You entered:", input_value)