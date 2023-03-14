import random

scissors = """
  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

"""
rock = """
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""
paper = """
 ________       
|        |     
|        |    
|        |       
|________|
"""

user = int(input("What do you choose? \n"
      "1 for rock\n"
      "2 for paper\n"
      "3 for scissors\n"))
pc = random.randint(0,2)
user -= 1

objects = [rock,paper,scissors]
user_sel = objects[user]
pc_sel = objects[pc]

if user_sel == rock:
    if pc_sel == rock:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"TIE! try again")
    elif pc_sel == paper:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a LOOSER!")
    elif pc_sel == scissors:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a WINNER!")
elif user_sel == paper:
    if pc_sel == rock:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a WINNER!")
    elif pc_sel == paper:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"TIE! try again")
    elif pc_sel == scissors:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a LOOSER")
elif user_sel == scissors:
    if pc_sel == rock:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a LOOSER!")
    elif pc_sel == paper:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"You are a WINNER")
    elif pc_sel == scissors:
        print(f"You chose {user_sel}\n")
        print(f"Computer chose {pc_sel}\n")
        print(f"TIE! try again")
else:
    print("INCORRECT SELECTION, TRY AGAIN PLEASE!")

