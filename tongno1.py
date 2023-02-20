def get_input():
    numbers = []
    while True:
        input_str = input("กรอกตัวเลขจำนวนจริงจำนวน 5 ตัวเลข : ")
        input_list = input_str.split()
        if len(input_list) == 5:
            try:
                numbers = [float(num) for num in input_list]
                break
            except ValueError:
                print("กรุณากรอกตัวเลขจำนวนจริง!")
        else:
            print("กรุณาเว้นวรรคระว่างตัวเลข")
    return numbers

numbers = get_input()
print("The numbers are:", numbers)