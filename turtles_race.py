from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500,height=400,startx=800,starty=0)

#method for screen
number = screen.textinput(title='Number of competitors',prompt='How many competitors compete? Give a number from 2 to 6: ')
colors = ['red','orange','yellow','green','blue','purple']
user_bet_1 = screen.textinput(title='Make your bet, player 1',prompt='Which turtle win the race? Enter a color from\n'
                            f'{colors[0:int(number)]}: ')
user_bet_2 = screen.textinput(title='Make your bet, player 2',prompt='Which turtle win the race? Enter a color from\n'
                            f'{colors[0:int(number)]}: ')

def pos_turtles(turtle_list):
    for pos in range(len(turtle_list)):
        turtle_list[pos].color(colors[pos-1])
        turtle_list[pos].penup()
        temp_pos = pos
        temp_pos *= 33.33
        turtle_list[pos].goto(x=-230,y=-100+temp_pos)
        
def turtles_competitors(number):
    turtles_list = []
    for _ in range(int(number)):
        turtle = Turtle(shape='turtle')
        turtles_list.append(turtle)
    pos_turtles(turtles_list)
    return turtles_list

turtles_list = turtles_competitors(number)
is_race_on = False

if (user_bet_1 in colors) & (user_bet_2 in colors):
    is_race_on = True
else:
    print('wrong entries, try again')
while is_race_on:
    for turtle in turtles_list:
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor()>230:
            if turtle.pencolor() == user_bet_1:
                print(f"Player 1 have won!, the {turtle.pencolor()} turtle wins.")
            elif turtle.pencolor() == user_bet_2:
                print(f"Player 1 have won!, the {turtle.pencolor()} turtle wins.")
            else:
                print(f"Anyone have won, LOOSERS :D")
            is_race_on = False
            break

screen.exitonclick()