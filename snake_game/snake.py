from turtle import Turtle, Screen
from food import Food
from animation import Animator
from time import sleep
from scores import Score
# from options import Popup
import tkinter as tk

class Snake:
    
    def __init__(self,no_of_units = 2, color = "white", speed = "medium"):
        self.set_screen()
        self.animator = Animator()
        self.add_food()
        self.no_of_snake_unit = no_of_units
        self.snake_color = color
        self.prepare_snake_units()
        self.score_board=Score()
        self.game_screen.update()
        self.grabbed_food = []
        self.speed=speed
            
    def set_screen(self):
        self.game_screen = Screen()
        self.game_screen.setup(600,600)
        self.game_screen.bgcolor("black")
        self.game_screen.title("Snake Game")
        self.game_screen.tracer(0)


    def add_food(self):
        self.food = Food()

    def prepare_snake_units(self):
        self.snake_head = Turtle(shape="square")
        self.snake_head.color(self.snake_color)
        self.snake_head.penup()
        self.snake_units=[self.snake_head]
        for i in range(self.no_of_snake_unit):
            print("snake unit added")
            self.add_snake_unit()
            self.set_initial_position()
            
    def add_snake_unit(self):
        new_snake_unit = Turtle("square")
        new_snake_unit.color(self.snake_color)
        new_snake_unit.penup()
        new_snake_unit.goto(self.snake_units[-1].xcor(),self.snake_units[-1].ycor())
        self.snake_units.append(new_snake_unit)

    def set_initial_position(self):
        x = 0
        y = 0
        for snake_unit in self.snake_units:
            snake_unit.goto(x, y)
            x -= 20

    def start_moving(self):
        self.game_over = False
        self.continue_game = True
        while not self.game_over and self.continue_game:
            self.score_board.show_scores(len(self.grabbed_food))
            self.move_one_step()
            self.print_coords()
            self.get_snake_head_coords()
            self.game_screen.listen()
            self.game_screen.onkey(self.head_north, "Up")
            self.game_screen.onkey(self.head_west, "Left")
            self.game_screen.onkey(self.head_south, "Down")
            self.game_screen.onkey(self.head_east, "Right")
            self.game_screen.onkey(self.pause_or_resume, "space")
            self.game_screen.onkey(self.replay,"r")
            self.game_screen.onkey(self.quit,"Escape")
            
            if self.check_for_food():
                self.add_snake_unit()
                self.add_food()
            sleep(self.set_speed())
            self.game_screen.update()

            self.check_overlapping()
            self.check_boundry()


    def get_snake_head_coords(self):
        x = round(self.snake_head.xcor())
        y = round(self.snake_head.ycor())
        snake_head_coords = (x, y)
        return snake_head_coords

    def print_coords(self):
        snake_head_coords=self.get_snake_head_coords()
        print(f"food = {self.food.food_coords}")
        print(f"snake = {snake_head_coords}")

    def move_one_step(self):
        for index in range(len(self.snake_units)-1,0,-1):
            new_x = self.snake_units[index - 1].xcor()
            new_y = self.snake_units[index - 1].ycor()
            self.snake_units[index].goto(new_x, new_y)
        self.snake_head.forward(20)

    def check_overlapping(self):
        for snake_unit in self.snake_units[1:]:
            x = round(snake_unit.xcor())
            y = round(snake_unit.ycor())
            unit_coords = (x, y)
            if self.get_snake_head_coords()==unit_coords:
                self.game_over=True
                self.game_over_func()

    def check_boundry(self):
        x = self.get_snake_head_coords()[0]
        y = self.get_snake_head_coords()[1] 
        if x>=300 or x<=-300 or y>=300 or y<=-300:
            self.game_over=True
            self.game_over_func()

    def game_over_func(self):
        self.animator.print_message("Game Over!")
        self.animator.penup()
        self.animator.goto(self.animator.xcor(),-60)
        self.animator.pendown()
        self.animator.print_message("press 'escape' to quit or 'r' to replay", fontsize=20)
        print("Game Over")

    def replay(self):
        print("replay...")
        game_over=True
        self.game_screen.clear()
        snake = Snake(color = self.snake_color, speed = self.speed)
        snake.start_moving()
        self.game_screen.update()

    def set_speed(self):
        if self.speed=="fast":
            return 0.1
        elif self.speed=="medium":
            return 0.4
        elif self.speed=="slow":
            return 0.8
        else:
            return 0.4

    def grab_food(self):
        self.food.hideturtle()
        self.grabbed_food.append(self.food)


    def check_for_food(self):
        if self.get_snake_head_coords()==self.food.food_coords:
            self.grab_food()
            print("food grabbed")
            return True
        else:
            return False

    def head_east(self):
        if self.snake_head.heading() != 180:
            print("heading east")
            self.snake_head.setheading(0)

    def head_north(self):
        if self.snake_head.heading() != 270:
                print("heading north")
                self.snake_head.setheading(90)

    def head_west(self):
        if self.snake_head.heading() != 0:
            print("heading west")
            self.snake_head.setheading(180)

    def head_south(self):
        if self.snake_head.heading() != 90:
            print("heading south")
            self.snake_head.setheading(270)

    def pause_or_resume(self):
        if not self.game_over:
            if self.continue_game==True:
                self.animator.print_message("Game Paused")
                print("pause request recieved!")
                self.continue_game = False
            else:
                self.animator.clear()
                self.animator.print_message("Game Resumed")
                sleep(0.5)
                self.animator.clear()
                print("resume request recieved!")
                self.continue_game = True
                self.start_moving()
    
    def quit(self):
        print("exiting...")
        exit()
            
