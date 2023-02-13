import sys
# sys.stdout.write("Hello World")

def atd_command(text):
    sys.stdout.write(text + '\n')

for i  in range(0,10):
 double = i * 2
 atd_command(i)