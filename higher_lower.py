from random import randint as rint
from art import higher_lower as hl
from art import vs
from os import system
from game_data import data as game_data

def get_person_data():
    person = rint(0,len(game_data)-1)
    return person

def get_person_2_data(person):
    person_2 = rint(0,len(game_data)-1)
    while person == person_2:
        person_2 = rint(0,len(game_data)-1)
    return person_2
system("cls")
person_a = get_person_data()
person_b = get_person_2_data(person_a)

score = 0
start_game = True
print(f"{hl}\nCompare A: {game_data[person_a]['name']},{game_data[person_a]['description']},from {game_data[person_a]['country']}")
print(f"{vs}\nCompare B: {game_data[person_b]['name']},{game_data[person_b]['description']},from {game_data[person_b]['country']}")
followers = input("Who has more followers? Type 'A' or 'B': ").upper()
while start_game:
    if followers == 'A':
        if game_data[person_a]['follower_count']>game_data[person_b]['follower_count']:
            score += 1
            person_b = get_person_2_data(person_a)
            system("cls")
            print(f"{hl}\nYou're right! Current score: {score}")
            print(f"Compare A: {game_data[person_a]['name']},{game_data[person_a]['description']},from {game_data[person_a]['country']}")
            print(f"{vs}\nCompare B: {game_data[person_b]['name']},{game_data[person_b]['description']},from {game_data[person_b]['country']}")
            followers = input("Who has more followers? Type 'A' or 'B': ").upper()
            if score == 10:
                system("cls")
                print(f"{hl}\nYou Win, Final score: {score}")
                break
        else:
            system("cls")
            print(f"{hl}\nSorry, that's wrong. Final score: {score}")
            break
    elif followers == 'B':
        if game_data[person_b]['follower_count']>game_data[person_a]['follower_count']:
            score += 1
            person_a = person_b
            person_b = get_person_2_data(person_a)
            system("cls")
            print(f"{hl}\nYou're right! Current score: {score}")
            print(f"Compare A: {game_data[person_a]['name']},{game_data[person_a]['description']},from {game_data[person_a]['country']}")
            print(f"{vs}\nCompare B: {game_data[person_b]['name']},{game_data[person_b]['description']},from {game_data[person_b]['country']}")
            followers = input("Who has more followers? Type 'A' or 'B': ").upper()
            if score == 10:
                system("cls")
                print(f"{hl}\nYou Win, Final score: {score}")
                break
        else:
            system("cls")
            print(f"{hl}\nSorry, that's wrong. Final score: {score}")
            break
    else:
        print(f"please, TYPE 'A' or 'B'")
        followers = input("Who has more followers? Type 'A' or 'B': ").upper()