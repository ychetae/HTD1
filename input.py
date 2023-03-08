import string
def get_alpha_only():
    user_input = input("Please enter only alphabetical characters: ")
    sw = user_input[-1] + user_input[1:-1] + user_input[0]
    if all(c in string.ascii_letters for c in user_input):
        print(sw)
    else:
        print("Invalid Input")

get_alpha_only()