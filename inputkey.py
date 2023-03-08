while True:
    input_string = input("ป้อนชื่อภาษาอังกฤษ : ")
    result = ""
    for char in input_string:
        if char.isalpha() or char.isspace():
            result += char
        else:
            break

    if len(result) == len(input_string):
        print("สวัสดีคุณ :", result.replace(" ", "  "))
        break
    else:
        print("ไม่สามารถใส่ตัวเลขได้ กรุณากรอกใหม่อีกครั้งหนึ่ง")