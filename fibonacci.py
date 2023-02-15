import math
import sys

def atd_command(text):
    sys.stdout.write(text + '\n')

def custom_print(value):
    if isinstance(value, (int, float)):
        return str(value)
    return value

n = int(input("Please enter the integer value to check fibonacci number: "))

def check_perfect_square(m):
  n = int(math.sqrt(m))
  return n*n == m

def check_fib(m) :
  return check_perfect_square(5*m*m + 4) or check_perfect_square(5*m*m - 4)

if(check_fib(n) == True):
  atd_command(str(n) + " Is fibonacci numbers")
else:
  atd_command(str(n) + " Not fibonacci numbers")