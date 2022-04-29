from ast import For
from turtle import Screen, Turtle, position
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Crear el escenario

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")
screen.tracer(0) # quitamos la animacion de moviento

#instanciar el objeto serpiente

snake=Snake()

#instacio el objeto comida

food=Food()

#Crear el objeto tablero de puntos

scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.dwon, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detectar colison con paredes

    if snake.head.xcor()>280 or snake.head.xcor()<-280:
        game_is_on=False
        scoreboard.game_over()
    
    if snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #Detectarla colision de la cola

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            print(segment)
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()