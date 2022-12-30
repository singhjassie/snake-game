from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8)
        self.color("yellow")
        self.penup()
        self.add_food()

    def add_food(self):
        x = randrange(-280, 281, 20)
        y = randrange(-280, 281, 20)
        self.food_coords = (x, y)
        self.goto(self.food_coords)
