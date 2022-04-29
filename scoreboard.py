from turtle import Turtle

ALING="center"
FONT=("Arial", 25, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0 #atributo
        #self.goto(0,-270)
        self.goto(-200,-270)
        self.color("white")
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        #self.write(f"Points: {self.score}",font=FONT,align=ALING)
        self.write(f"Points: {self.score}",font=FONT)
    
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Juego terminado :V",font=FONT,align=ALING)
        