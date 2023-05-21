#Password Generator Project
import random

def random_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','_']

    temporal_letters = [random.choice(letters) for letter in range(1,random.randint(8,10)+1)] 
    temporal_numbers = [random.choice(numbers) for number in range(1,random.randint(2,4)+1)] 
    temporal_symbols = [random.choice(symbols) for symbol in range(1,random.randint(2,4)+1)] 

    password = temporal_letters + temporal_numbers + temporal_symbols
    random.shuffle(password)

    password = ''.join(password)

    return password