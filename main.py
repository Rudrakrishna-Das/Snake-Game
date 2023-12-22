from turtle import Screen
from snake import Snake
from food import Food
from scorebord import Scorebord
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Scorebord()

screen.listen()

screen.onkeypress(key='Up',fun=snake.up)
screen.onkeypress(key='Down',fun=snake.down)
screen.onkeypress(key='Left',fun=snake.left)
screen.onkeypress(key='Right',fun=snake.right)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #eat food
    if snake.head.distance(food) < 15:
        score.clear()
        score.update_score()
        snake.extend()
        food.refresh()
    
    #Detect wall touch
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_is_on = False
        score.game_over() 
    
    #Detect snake touch own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    



screen.exitonclick()