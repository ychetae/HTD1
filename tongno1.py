def get_input():
    numbers = []
    count = 0
    while count < 5:
        try:
            num = float(input("Enter a real number: "))
            numbers.append(num)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a real number.")
    return numbers

numbers = get_input()
if len(numbers) == 5:
    # Do something with the numbers here
    print("The numbers are:", numbers)
else:
    print("Number of inputs is less than 5.")