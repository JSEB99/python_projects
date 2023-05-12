from turtle import Turtle, Screen
from car import Car
from cars import Traffic
from random import randint,randrange
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('white')
screen.tracer(0)


car = Car()
screen.listen()
screen.onkey(fun=car.up,key='Up')
traffic = Traffic()
level = Scoreboard()

game_is_on = True
level_velocity = 0.1

while game_is_on:
    screen.update()
    time.sleep(level_velocity)
    traffic.moving()
    lines_value = len(traffic.lines)
    if traffic.lines[-1][-1].xcor()<randrange(200,260,3):
        traffic.create_car()
    for set_of_cars in traffic.lines:
        for vehicles in traffic.cars_in_street:
            if car.distance(vehicles) < 15:
                level.game_over()
                game_is_on = False
                break
    if car.ycor()>280:
        level.increase_points()
        car.next_level()
        level_velocity *= 0.7

screen.exitonclick()