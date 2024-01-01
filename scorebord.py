from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ('Arial',12,'normal')

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.read_high_score()
        self.create_score()
       

    def read_high_score(self):
        try:
            with open('high_score.txt',mode='r') as file:
                high_score = int(file.read())
                self.high_score = high_score
        except:
            with open('high_score.txt',mode='w') as file:
                file.write('0')

            with open('high_score.txt',mode='r') as file:
                high_score = int(file.read())
                self.high_score = high_score


    def create_score (self):
        self.clear()
        self.penup()
        self.goto(x=100,y=280)
        self.color('white')
        self.hideturtle()
        self.write(f'Score : {self.score} High Score : {self.high_score}',align=ALLIGNMENT,font=FONT)

    def reset_score(self):
        with open('high_score.txt',mode='w') as file: 
            file.write(str(self.high_score))      
        self.score = 0        
        self.create_score()


    # def game_over (self):
    #     self.goto(x=0,y=0)
    #     self.write("GAME OVER",align=ALLIGNMENT,font=FONT)

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.create_score()