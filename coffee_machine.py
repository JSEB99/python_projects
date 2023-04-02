from coffee_machine_data import resources
from coffee_machine_data import MENU
from os import system as sys
from art import coffe_text

def check_resources(user_decision):
    resources_ind = 1
    global resources
    if user_decision == 'espresso':
        if resources['water']-MENU[user_decision]['ingredients']['water']>=0:
            if resources['coffee']-MENU[user_decision]['ingredients']['coffee']<0:
                print('Sorry there is not enough coffee.')
                input()
                resources_ind = 0
        else:
            print('Sorry there is not enough water.')
            input()
            resources = 0
    elif user_decision == 'cappuccino' or user_decision == 'latte':
        if resources['water']-MENU[user_decision]['ingredients']['water']>=0:
            if resources['coffee']-MENU[user_decision]['ingredients']['coffee']>=0:
                if resources['milk']-MENU[user_decision]['ingredients']['milk']<0:
                    print('Sorry there is not enough milk.')   
                    input()
                    resources_ind = 0
            else:
                print('Sorry there is not enough coffee.')
                input()
                resources_ind = 0
        else:
            print('Sorry there is not enough water.')
            input()
            resources_ind = 0
    return resources_ind
def insert_coins(user_decision,change,money):
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    coins = (quarters*0.5)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    if MENU[user_decision]['cost']<=coins:
        change = coins - MENU[user_decision]['cost']
        money = MENU[user_decision]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
        input()
        change = 0
    return change,money
money,change = 0,0
start_machine = 'ON'
coins = {
    "quarters":0.25,
    "dimes":0.10,
    "nickles":0.05,
    "pennies":0.01
}
while start_machine == 'ON':
    sys("cls")
    print(coffe_text)
    user_decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
    decision = check_resources(user_decision)
    if user_decision == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(money,2)}")
        input()
    elif user_decision.upper() == 'OFF':
        start_machine = 'OFF'
    if decision == 1 and user_decision in MENU.keys():
        temp_money = money
        change,money = insert_coins(user_decision,change,money)
        if temp_money < money:
            if user_decision == 'espresso':
                resources['water']=resources['water']-MENU[user_decision]['ingredients']['water']
                resources['coffee']=resources['coffee']-MENU[user_decision]['ingredients']['coffee']
            elif user_decision == 'latte' or user_decision == 'cappuccino':
                resources['water']=resources['water']-MENU[user_decision]['ingredients']['water']
                resources['coffee']=resources['coffee']-MENU[user_decision]['ingredients']['coffee']
                resources['milk']=resources['milk']-MENU[user_decision]['ingredients']['milk']
            print(f"Here is ${round(float(change),2)} in change\n")
            print(f"Here is your {user_decision} ☕. Enjoy!")
            input()
    


