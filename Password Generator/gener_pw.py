# Password Generator with hardcoded Character (8) limit
from random import randint, choice

def generate_password(elements):
    candidate = ""
    for i in range(8):
        candidate += choice(elements[:])
    
    passwords.append(candidate)


possible_characters = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]

chars_w_symbols = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D", "=", "!", "@", "#", "$", "%", "^", "&", "*", "/", "?"]

passwords = list()

user_range = int(input("How many passwords would you like? "))

user_choice = input("Do you want symbols in the password? (y/n) ")

if user_choice == 'y':
    for i in range(1,user_range + 1):  
        generate_password(chars_w_symbols)

if user_choice == 'n':
    for i in range(1,user_range + 1):  
        generate_password(possible_characters)

num = 1
for i in passwords:  
    print(f"{num}: {i}")
    num = num + 1
