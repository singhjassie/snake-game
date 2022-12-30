#!/usr/bin/python3.9
from snake import Snake
from screen_animation import ScreenAnimation
from options import Settings
from turtle import Screen

SNAKE_SPEED = "medium"
SNAKE_COLOR = "white"

animation = ScreenAnimation()
game_screen = Screen()
game_screen.title("Snake Game")
show_options=True
while show_options:
        animation.starting_animation()
        if animation.selected_option=="start":
                show_options=False
        elif animation.selected_option=="settings":
                back = False
                while not back:
                        settings = Settings()
                        if settings.selected_option=="resume":
                                back = True
                        if settings.selected_option=="speed":
                                settings.speed()
                                if settings.selected_option=="slow":
                                        SNAKE_SPEED="slow"
                                elif settings.selected_option=="medium":
                                        SNAKE_SPEED="medium"
                                elif settings.selected_option=="fast":
                                        SNAKE_SPEED="fast"
                        elif settings.selected_option=="snake color":
                                settings.snake_color()
                                if settings.selected_option=="yellow":
                                        SNAKE_COLOR="yellow"
                                elif settings.selected_option=="red":
                                        SNAKE_COLOR="red"
                                elif settings.selected_option=="green":
                                        SNAKE_COLOR="green"
        elif animation.selected_option=="quit":
                print("exiting...")
                exit()

animation.clear_screen()
animation.start_count()
snake = Snake(color=SNAKE_COLOR, speed= SNAKE_SPEED) 
snake.start_moving()



game_screen.exitonclick()