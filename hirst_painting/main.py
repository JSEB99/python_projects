import colorgram
import turtle as t
from random import choice
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    if r<240 or g<240 or b<240:
        rgb_colors.append((r,g,b))
t.colormode(255)
dot = t.Turtle()
dot.hideturtle()
dot.shape("circle")
dot.speed("fast")
dot.penup()
dot.setheading(225)
dot.forward(320)
dot.setheading(0)
def square(num_dots):
    initial_pos = list(dot.position())
    for i in range(num_dots):
        for j in range(num_dots):
            dot.pendown()
            dot.dot(20,choice(rgb_colors))
            dot.penup()
            dot.forward(50)
        if i < (num_dots-1):
            initial_pos[1] += 50
            dot.setpos(initial_pos[0],initial_pos[1])

screen = t.Screen()
screen.setup(width=520,height=520)  
screen.bgcolor("LightGray")
screen.title("Hirst Painting")
square(10)

screen.exitonclick()

