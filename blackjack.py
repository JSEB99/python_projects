#Blackjack game
from random import randint,choice
from os import system as sys
from art import blackjack_title as bjtitle
from art import skull as sk
from art import tie,money
import time
#get the cards
def blackjack(cards,card_temp):
    card_list=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    for card in range(cards):
        cards=choice(card_list)
        card_temp.append(cards)
    return card_temp
#decide who wins
def winner(user_counter,dealer_counter,user,dealer):
    if user_counter==21 and dealer_counter==21:
        user_length = len(user)
        dealer_length = len(dealer)
        if user_length>dealer_length:
            print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
            final_result=2
        elif user_length<dealer_length:
            print(f"User wins!\nuser: {user}\ndealer: {dealer}")
            final_result=1
        else:
            print(f"Tie!\nuser: {user}\ndealer: {dealer}")
            final_result=0
    elif user_counter>21 and dealer_counter>21:
        user_length = len(user)
        dealer_length = len(dealer)
        if user_length>dealer_length:
            print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
            final_result=2
        elif user_length<dealer_length:
            print(f"User wins!\nuser: {user}\ndealer: {dealer}")
            final_result=1
        else:
            print(f"Tie, Anyone wins!\nuser: {user}\ndealer: {dealer}")
            final_result=0
    elif user_counter<=21 and dealer_counter>21:
        print(f"User wins!\nuser: {user}\ndealer: {dealer}")
        final_result=1
    elif user_counter>21 and dealer_counter<=21:
        print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
        final_result=2
    elif user_counter==21 and dealer_counter<21:
        print(f"User wins!\nuser: {user}\ndealer: {dealer}")
        final_result=1
    elif user_counter<21 and dealer_counter==21:
        print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
        final_result=2
    elif user_counter>dealer_counter:
        print(f"User wins!\nuser: {user}\ndealer: {dealer}")
        final_result=1
    elif dealer_counter>user_counter:
        print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
        final_result=2
    elif dealer_counter==user_counter:
        user_length = len(user)
        dealer_length = len(dealer)
        if user_length>dealer_length:
            print(f"Dealer wins!\nuser: {user}\ndealer: {dealer}")
            final_result=2
        elif user_length<dealer_length:
            print(f"User wins!\nuser: {user}\ndealer: {dealer}")
            final_result=1
        else:
            print(f"Tie, Anyone wins!\nuser: {user}\ndealer: {dealer}")
            final_result=0
    return final_result
#decide the value of the As
def As(person,person_list):
    if person==1:
        if 1 in person_list:
            print(person_list)
            user_decision=input("Do you want As=1 or As=11? Y=1 of N=11: ").upper()
            if user_decision=='N':
                user_as=person_list.index(1)
                person_list[user_as]=11
    if person==2:
        if (sum(person_list)+11)<=21:
            dealer_des=11
        else:
            dealer_des=1
        if 1 in person_list:
            print(person_list)
            dealer_as=person_list.index(1)
            person_list[dealer_as]=dealer_des
    return person_list
#decide if the user or the dealer wants more cards
def blackjack_game(start_point):
    if start_point=='Y':
        user=[]
        dealer=[]
        print(bjtitle)
        user=blackjack(2,user)
        dealer=blackjack(2,dealer)
        print(f"User cards: {user}\nDealer 1st card: {dealer[0]}")
        user=As(1,user)
        dealer=As(2,dealer)
        user_counter=sum(user)
        dealer_counter=sum(dealer)
        sys("cls")
        print(bjtitle)
        print(f"RESUME\nuser cards: {user}\ndealer cards: {dealer}")
        user_continue = input("Do you want to request for another card? Y/N: ").upper()
        sys("cls")
        while user_continue=='Y':
            print(bjtitle)
            user=blackjack(1,user)
            user=As(1,user)
            user_counter=sum(user)
            dealer_counter=sum(dealer)
            print(f"RESUME\nuser cards: {user}\ndealer cards: {dealer}")
            if user_counter>21:
                user_continue='N'
            else:
                user_continue = input("Do you want to request for another card? Y/N: ").upper()
            sys("cls")
        dealer_counter=sum(dealer)
        user_counter=sum(user)
        if user_counter<21:
            if user_counter==dealer_counter:
                user_length=len(user)
                dealer_length=len(dealer)
                if user_length<dealer_length:
                    while dealer_counter<17 or ((dealer_counter<user_counter) and 
                        user_counter<=21) or ((user_counter==dealer_counter) and user_counter<21):
                        dealer=blackjack(1,dealer)
                        dealer=As(2,dealer)
                        dealer_counter=sum(dealer)
                        if dealer_counter>=21:
                            break
                        print(f"RESUME\nuser cards: {user}\ndealer cards: {dealer}")
                        sys("cls")
            else:
                while dealer_counter<17 or ((dealer_counter<user_counter) and 
                    user_counter<=21) or ((user_counter==dealer_counter) and user_counter<21):
                    dealer=blackjack(1,dealer)
                    dealer=As(2,dealer)
                    dealer_counter=sum(dealer)
                    if dealer_counter>=21:
                        break
                    print(f"RESUME\nuser cards: {user}\ndealer cards: {dealer}")
                    sys("cls")
        user_counter=sum(user)
        dealer_counter=sum(dealer)
        sys("cls")
        print(bjtitle)
        final_draw=winner(user_counter,dealer_counter,user,dealer)
        if final_draw==1:
            print(money)
        elif final_draw==2:
            print(sk)
        elif final_draw==0:
            print(tie)
        start_point=input("Do you want to play again? Y/N: ").upper()
        if start_point=='Y':
            sys("cls")
            blackjack_game(start_point)
    if start_point=='N':
        print("Sorry, see you the next time you want to play! :D\n"
              "The game is going to close in 5 seconds.")
        time.sleep(5)
        sys("cls")
sys("cls")
print(bjtitle)
start_point=input("Do you want to play? Y/N: ").upper()
sys("cls")
blackjack_game(start_point)




