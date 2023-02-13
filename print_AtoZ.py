import sys

def atd_command(text):
    sys.stdout.write(text + '\n')

def atd_command_letters_a_to_z():
    for letter in range(ord('A'), ord('Z')+1):
        atd_command(chr(letter))

atd_command_letters_a_to_z()