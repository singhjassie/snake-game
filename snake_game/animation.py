#!python3.9
from turtle import Turtle, Screen


class Animator(Turtle):

    def __init__(self,color = "white"):
        super().__init__()
        self.animator_color = color
        self.add_animator(self.animator_color)

    def add_animator(self, color):
        self.hideturtle()
        self.color(color)

    def print_message(self, message, fontsize=40, alignment="center"):
        self.write(message, align=alignment, font=(
            "Times New Roman", fontsize, "normal"))


class AnimatorSnake:

    def __init__(self, no_of_units=2, snake_color="white", starting_coords=(-300, 20), head="east"):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(600, 600)
        self.no_of_snake_unit = no_of_units
        self.snake_color = snake_color
        self.starting_coords = starting_coords
        self.head_direction = head
        self.prepare_snake_units()

    def prepare_snake_units(self):
        self.snake_head = Turtle(shape="square", visible=False)
        self.snake_head.color(self.snake_color)
        self.snake_head.penup()
        self.snake_units = [self.snake_head]
        for i in range(self.no_of_snake_unit):
            # print("snake unit added")
            self.screen.delay(0)
            self.add_snake_unit()
            self.screen.delay(0.5)
            self.set_initial_position()

    def add_snake_unit(self):
        new_snake_unit = Turtle("square", visible=False)
        new_snake_unit.color(self.snake_color)
        new_snake_unit.penup()
        new_snake_unit.goto(
            self.snake_units[-1].xcor(), self.snake_units[-1].ycor())
        self.snake_units.append(new_snake_unit)

    def set_initial_position(self):
        x = self.starting_coords[0]
        y = self.starting_coords[1]
        for snake_unit in self.snake_units:
            snake_unit.goto(x, y)
            if self.head_direction == "east":
                x -= 20
            elif self.head_direction == "north":
                self.snake_head.setheading(90)
                y -= 20
            elif self.head_direction == "south":
                self.snake_head.setheading(270)
                y += 20
            elif self.head_direction == "west":
                self.snake_head.setheading(180)
                x += 20
            snake_unit.showturtle()

    def move_one_step(self):
        for index in range(len(self.snake_units)-1, 0, -1):
            new_x = self.snake_units[index - 1].xcor()
            new_y = self.snake_units[index - 1].ycor()
            self.snake_units[index].goto(new_x, new_y)
        self.snake_head.forward(20)

    def head_east(self):
        # print("heading east")
        self.snake_head.setheading(0)

    def head_north(self):
        # print("heading north")
        self.snake_head.setheading(90)

    def head_west(self):
        # print("heading west")
        self.snake_head.setheading(180)

    def head_south(self):
        # print("heading south")
        self.snake_head.setheading(270)
