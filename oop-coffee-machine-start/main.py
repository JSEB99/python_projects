#classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system as sys
from art import coffee_text
start_machine = 'ON'
#objects
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while start_machine=='ON':
    sys("cls")
    print(coffee_text)
    user_decision = input(f"What would you like? {my_menu.get_items()}: ").lower()
    if user_decision == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        input("enter to continue...")
    elif user_decision == "off":
        start_machine = "off"
    elif user_decision in my_menu.get_items():
        drink = my_menu.find_drink(user_decision)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink) 
            input("enter to continue...")
        else:
            input("enter to continue...")

            

    