import sys


def atd_command(text):
    sys.stdout.write(text + " ")

def custom_print(value):
    if isinstance(value, (int, float)):
        return str(value)
        return value


def print_numbers():
  numbers = ""
  for i in range(10):
    numbers += custom_print(i)
    numbers += " "
  return numbers

atd_command(str(print_numbers()) + "bath")