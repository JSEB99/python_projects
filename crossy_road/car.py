from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_len=1,stretch_wid=0.5)
        self.color('red')
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
    
    def up(self):
        self.forward(10)
    
    def next_level(self):
        self.goto(0,-280)
   