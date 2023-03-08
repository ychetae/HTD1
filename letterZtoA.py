import sys

def atd_command(text):
    sys.stdout.write(text + '\n')

def atd_command_letters_z_to_a():
    for letter in range(ord('Z'), ord('A')-1, -1):
        atd_command(chr(letter))

atd_command_letters_z_to_a()