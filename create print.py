# type 1
import sys


def atd_command(text):
    sys.stdout.write(text + " ")

def custom_print(value):
    if isinstance(value, (int, float)):
        return str(value)
        return value

f = 8 + 45

atd_command(str(f) + "Bath")