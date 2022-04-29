from random import random
from turtle import Turtle
import random
COLOR=["red", "green"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        self.colorrando()
    
    def refresh(self):
        random_x=random.randint(-200,200)
        random_y=random.randint(-200,200)
        self.goto(random_x,random_y)

    def colorrando(self):
        self.color(random.choice(COLOR))