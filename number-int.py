def Number():
    while True:
        try:
            value = float(input("กรุณาป้อนจำนวนจริงไม่เกินหลักร้อย: "))
            if abs(value) <= 100:
                return value
            else:
                print("ค่าต้องไม่เกินหลักร้อย โปรดป้อนใหม่")
        except ValueError:
            print("ข้อมูลไม่ถูกต้อง โปรดป้อนใหม่")

value = Number()
print("ค่าที่ได้รับ: ", value)