from ast import Constant, For
from turtle import Turtle, position, right
import random
import numpy as np

STARTING_POSITION = np.array([(0,0),(-20,0),(-40,0),(-60,0),(-80,0),(-100,0),(-120,0),(-140,0),(-160,0)])
RIGHT, UP, LEFT, DOWN =[0,90,180,270]
COLOR=["red", "green","blue","yellow","orange","pink"]



class Snake:

    def __init__(self):
        self.segments=[]
        self.create__snake()
        self.head=self.segments[0]

    
    
    def create__snake(self):
        for position in STARTING_POSITION:
            snake_segment1=Turtle("square")
            snake_segment1.penup()
            snake_segment1.color(random.choice(COLOR))
            snake_segment1.goto(position)
            self.segments.append(snake_segment1)
    
    def add_segment(self,position):
        snake_segment1=Turtle("square")
        snake_segment1.penup()
        snake_segment1.color(random.choice(COLOR))
        snake_segment1.goto(position)
        self.segments.append(snake_segment1)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        

            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        
        self.head.forward(20)
        #self.head.left(90)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def dwon(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)





