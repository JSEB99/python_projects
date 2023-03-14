#encrypt or decrypt a message using a shift on a list :)
import art
def caesar(text,shift,direction):
    text_shifted = ''  
    for letter in text:
        letter_position = characters.index(letter)
        if direction=="encode":
            new_position = letter_position + shift
        if direction=="decode":
            new_position = letter_position - shift
        while new_position > (len(characters)-1):     #lenght - 1 of characters' list
            new_position -= len(characters)       #lenght of characters' list
        while new_position < (-1*len(characters)):    #lenght of characters' list
            new_position += (len(characters)+1)       #lenght + 1 of characters' list
        shift_position_letter = characters.index(characters[new_position])
        shift_text.append(characters[shift_position_letter])
    for letter in shift_text:
        text_shifted +=letter
    print(f"The encoded text is -->{text_shifted}")
def user_ask():
    global direction,text,shift
    indicator = True
    while indicator:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            indicator = False
        else:
            indicator = True
            print("decode or encode, anything else!")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
shift_text = []
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', ',', '!', '.', '?',
              ' ']
print(art.logo)
user_ask()
caesar(text,shift,direction)
ask_user = input("do you want to repeat? Y/N\n").upper()
while ask_user == "Y":
    shift_text = []
    user_ask()
    caesar(text,shift,direction)
    ask_user = input("do you want to repeat? Y/N\n").upper()

