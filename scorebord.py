from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ('Arial',12,'normal')

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.create_score()
       

    def create_score (self): 
        self.penup()
        self.goto(x=100,y=280)
        self.color('white')
        self.hideturtle()
        self.write(f'Score : {self.score}',align=ALLIGNMENT,font=FONT)
    def game_over (self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",align=ALLIGNMENT,font=FONT)

    def update_score(self):
        self.score += 1
        self.create_score()