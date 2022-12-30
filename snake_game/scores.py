#!python3.9
from animation import Animator

class Score(Animator):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.forward(260)
        self.pendown()

    def show_scores(self,score):
        self.clear()
        self.print_message(f"Score : {score*5}",fontsize=20)