#!python3.9
from animation import Animator
from screen_animation import ScreenAnimation 

class Settings(ScreenAnimation):

    def __init__(self):
        super().__init__()
        self.clear_screen()
        self.screen.tracer(0)
        self.color("red")
        self.print_message("SETTINGS")
        self.color("white")
        self.options=["Resume","Speed","Snake Color"]
        self.show_options(self.options)
        self.add_selector()
        self.select_options()
        self.screen.update()

    def speed(self):
        self.clear_screen()
        self.screen.tracer(0)
        self.home()
        self.color("red")
        self.print_message("SPEED")
        self.color("white")
        self.options=["Slow","Medium","Fast"]
        self.show_options(self.options)
        self.add_selector()
        self.select_options()
        self.screen.update()
    
    def snake_color(self):
        self.clear_screen()
        self.screen.tracer(0)
        self.home()
        self.color("red")
        self.print_message("COLOR")
        self.color("white")
        self.options=["Yellow","Red","Green"]
        self.show_options(self.options)
        self.add_selector()
        self.select_options()
        self.screen.update()




