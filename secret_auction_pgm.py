from os import system
import art
print(f"{art.logo2}\nWelcome to the secret auction program")
people = {}
more_bidders = True
name = input("What is your name?: ")
bid = float(input("What's your bid?: $"))
people[name]=bid
while more_bidders:
    decision = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if decision == 'yes':
        system("cls")
        name = input("What is your name?: ")
        bid = float(input("What's your bid?: $"))
        people[name]=bid
    if decision == 'no':
        system("cls")
        more_bidders = False
biggest_bid = 0
for key in people:
    value = people[key]
    if value>biggest_bid:
        biggest_key = key
        biggest_bid = value
print(f"The winner is {biggest_key} with a bid of ${biggest_bid}")
    

