from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Bebas Neue Normal',14)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('yellow')
        self.penup()
        self.goto(x=-15,y=280)
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f'Score= {self.score}',True,align=ALIGNMENT,font=FONT)
    
    def increase_points(self):
        self.score += 1 
        self.clear()
        self.goto(x=-15,y=280)
        self.update_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write('GAME OVER.',True,align=ALIGNMENT,font=FONT)
