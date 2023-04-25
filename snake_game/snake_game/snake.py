from turtle import Turtle

UP = 90 # NORTH
DOWN = 270 # SOUTH
LEFT = 180 # EAST
RIGHT = 0 # WEST
BODY_SIZE = 20 # SIZE OF SEGMENT

class Snake:

    def __init__(self):
        self.snake_list=[]
        self.create_snake()
        self.head = self.snake_list[0]
        self.speed = 20
        self.stop = 0

    def create_snake(self):
        """Create the snake at (0,0)"""
        for pos in range(3):
            pos *= BODY_SIZE
            snake_body = Turtle(shape='square')
            snake_body.penup()
            snake_body.color('green')
            snake_body.goto(x=0-pos,y=0)
            self.snake_list.append(snake_body)

    def add_segment(self,position):
        snake_body = Turtle(shape='square')
        snake_body.penup()
        snake_body.color('green')
        snake_body.goto(position)
        self.snake_list.append(snake_body)

    def move(self,velocity):
        """movement of the snake"""
        for segment in range(len(self.snake_list)-1,0,-1):
            self.snake_list[segment].goto(self.snake_list[segment-1].position())
        self.head.forward(velocity)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT: 
            self.snake_list[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def extend(self):
        """add new segment to snake"""
        self.add_segment(self.snake_list[-1].position())



            