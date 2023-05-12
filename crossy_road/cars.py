from turtle import Turtle
from random import randrange,choice,randint

COLORS = ['orange','yellow','black','blue','green']

class Traffic():
    def __init__(self):
        self.cars_in_street = []
        self.lines = []
        self.create_car()

    def create_car(self):
        rango = randint(4,8)
        for veh in range(rango):
            car = Turtle(shape='square')
            car.turtlesize(stretch_len=2,stretch_wid=1)
            car.setheading(180)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300,randrange(-260,260,20))
            self.cars_in_street.append(car)
            self.lines.append(self.cars_in_street)
        if len(self.lines)>30:
            self.lines=[]
            self.create_car()

    def moving(self):
        for vehicle in range(len(self.cars_in_street)):
            x = self.cars_in_street[vehicle].xcor()
            y = self.cars_in_street[vehicle].ycor()
            self.cars_in_street[vehicle].goto(x-5,y)


