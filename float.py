def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("ค่าไม่ถูกต้อง โปรดป้อนใหม่")

value = float_input("โปรดป้อนค่าที่ต้องการ: ")
print("ค่าที่่ได้รับคือ:", value)