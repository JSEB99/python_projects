from os import system
import art
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
def calculator():
    """
    basic calculator using recursivity
    """
    print(art.calculator)
    operation = {"+":add,
                "-":sub,
                "*":mul,
                "/":div}
    num1 = float(input("What's the first number?: "))
    decision = True

    while decision:
        system("cls")
        
        print(f"{art.calculator}\n first number is {num1}\n"
            "You can use the following operations")
        for symbol in operation:
            print(f"--->{symbol}")

        operation_pick = input("Pick an operation from the line above: ")
        num2 = float(input("What's the third number?: "))
        first_answer = round(operation[operation_pick](num1,num2),3)
        print(f"{num1} {operation_pick} {num2} = {first_answer}")

        num1 = first_answer

        ask_user = input(f"Type 'y' to continue calculating with {num1},"
                    " type n to exit, or type r to start again: ")
        if ask_user == 'y':
            decision = True
        elif ask_user == 'n':
            break
        elif ask_user == 'r':
            calculator()
calculator()