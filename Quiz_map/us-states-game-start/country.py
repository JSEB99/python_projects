from turtle import Turtle

def write_country(x,y,state):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.color("black")
    text.goto(x,y)
    text.write(state)


