#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_output = [letters,numbers,symbols]
Password_lenght = nr_numbers + nr_symbols + nr_letters
temporal_output = []
password = ""
if Password_lenght==0:
    print("Zero is invalid for each question")
else:
    for letter in range(1,nr_letters+1):
        dice = random.choice(letters)
        temporal_output.append(dice)
    for number in range(1,nr_numbers+1):
        dice = random.choice(numbers)
        temporal_output.append(dice)
    for symbol in range(1,nr_symbols+1):
        dice = random.choice(symbols)
        temporal_output.append(dice)
    for output in range(1,len(temporal_output)+1):
        dice = random.choice(temporal_output)
        temporal_output.remove(dice)
        str_character = str(dice)
        password += str_character
    print(f"Here is your password: {password}")




