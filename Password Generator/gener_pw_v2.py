# Password Generator
from random import randint, choice

def generate_password(elements, size):
    candidate = ""
    for i in range(size):
        candidate += choice(elements[:])
    
    passwords.append(candidate)

numbers = ["0","1","2","3","4","5","6","7","8","9"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_alphabet = [char.lower() for char in alphabet]
symbols = ["=", "!", "@", "#", "$", "%", "^", "&", "*", "/", "?", "(", ")", "<", ">"]

passwords = list()

user_range = int(input("How many passwords would you like? "))
pw_size = int(input("How long do you want the password to be? (ex: 5 characters long) "))

user_choice_alphabet = input("Do you want the alphabet in the password? (y/n) ")

if user_choice_alphabet.lower() == 'y':
    user_choice_caps = int(input("Do you want all capital letters, all lowercase letters or a mix of both?\n1 - All Uppercase\n2 - All Lowercase\n3 - Both\n--> "))
    if user_choice_caps == 1:
        temp_list = alphabet
    elif user_choice_caps == 2:
        temp_list = lowercase_alphabet
    elif user_choice_caps == 3:
        temp_list = alphabet + lowercase_alphabet
    else:
        print("Invalid Choice --> Setting as BOTH")
        temp_list = alphabet + lowercase_alphabet

user_choice_numbers = input("Do you want numbers in the password? (y/n) ")
user_choice_symbols = input("Do you want symbols in the password? (y/n) ")

# ALL
if user_choice_alphabet.lower() == 'y' and user_choice_numbers.lower() == 'y' and user_choice_symbols.lower() == 'y':
    temp_list = temp_list + numbers + symbols
    for i in range(1, user_range + 1):
        generate_password(temp_list, pw_size)

# ONLY ALPHABET
if user_choice_alphabet.lower() == 'y':
    # IF ALPHABET AND NUMBERS
    if user_choice_numbers.lower() == 'y':
        temp_list = temp_list + numbers
        for i in range(1, user_range + 1):
            generate_password(temp_list, pw_size)
    # IF ALPHABET AND SYMBOLS
    if user_choice_symbols.lower() == 'y':
        temp_list = temp_list + symbols
        for i in range(1, user_range + 1):
            generate_password(temp_list, pw_size)
    for i in range(1, user_range + 1):
        generate_password(temp_list, pw_size)

# ONLY NUMBERS
if user_choice_numbers.lower() == 'y':
    # IF NUMBERS AND SYMBOLS
    if user_choice_symbols == 'y':
        temp_list = numbers + symbols
        for i in range(1, user_range + 1):
            generate_password(temp_list, pw_size)
    for i in range(1, user_range + 1):
        generate_password(numbers, pw_size)

# ONLY SYMBOLS
if user_choice_symbols.lower() == 'y':
    for i in range(1, user_range + 1):
        generate_password(symbols, pw_size)

num = 1
for i in passwords:
    print(f"{num}: {i}")
    num = num + 1
    if num > user_range:
        break
