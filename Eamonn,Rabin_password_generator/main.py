# password generator
# eamonn patterson, Rabin
# INFT 1207-01
# 1/26/2024
#########
import random
import string



while True:
    pass_length = input('Enter the length of the password: ')

    if int(pass_length) < 8:
        print('Please enter a value greater than or equal to 8.')
    else:
        break

remaining = int(pass_length)

while True:
    number_letters = input('How many letters should be in the password: ')
    if 0 <= int(number_letters) <= remaining:
        remaining -= int(number_letters)
        break
    else:
        print(f'Number of letters should be between 0 and {remaining}.')

while True:
    number_digits = input('How many digits should be in the password: ')
    if 0 <= int(number_digits) <= remaining:
        remaining -= int(number_digits)
        break
    else:
        print(f'Please enter a value between 0 and {remaining}.')

while True:
    number_special = input('How many special characters should be in the password: ')
    if 0 <= int(number_special) <= remaining:
        remaining -= int(number_special)
        break
    else:
        print(f'Please enter a value between 0 and {remaining}.')

def generate_pass(length, num_letter, num_digits, num_special):
    letter = ''.join(random.choices(string.ascii_letters, k=int(num_letter)))
    digit = ''.join(random.choices(string.digits, k=int(num_digits)))
    special = ''.join(random.choices(string.punctuation, k=int(num_special)))
    password = list(letter + digit + special)
    random.shuffle(password)
    return ''.join(password)

# Generate and print the password
print(generate_pass(pass_length, number_letters, number_digits, number_special))
