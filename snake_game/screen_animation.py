from animation import AnimatorSnake, Animator
from turtle import Screen
from time import sleep

class Selector(Animator):
    
    def __init__(self,coords):
        super().__init__()
        self.color("white")
        self.selector_coords = coords
        self.add_selector()

    def add_selector(self):
        self.pensize(4)
        self.penup()
        self.goto(self.selector_coords)
        self.pendown()
        self.setheading(0)
        self.begin_fill()
        self.forward(225)
        self.setheading(270)
        self.forward(48)
        self.setheading(180)
        self.forward(225)
        self.setheading(90)
        self.forward(48)


class ScreenAnimation(Animator):

    def __init__(self):
        super().__init__()
        self.screen = Screen()

    def starting_animation(self):
        self.clear_screen()
        self.draw_s()
        self.draw_n()
        self.draw_a()
        self.draw_k()
        self.draw_e()
        self.add_selector()
        self.options=["Start", "Settings", "Quit"]
        self.show_options(self.options)
        self.select_options()
        # self.clear_screen()
        # self.start_count()


    def draw_s(self):
        snake = AnimatorSnake(no_of_units = 17, snake_color="red")
        for step in range(6):
            snake.move_one_step()
        snake.head_north()
        for step in range(3):
            snake.move_one_step()
        snake.head_west()
        for step in range(3):
            snake.move_one_step()
        snake.head_north()
        for step in range(3):
            snake.move_one_step()
        snake.head_east()
        for step in range(3):
            snake.move_one_step()

    def draw_n(self):
        snake = AnimatorSnake(no_of_units = 9, snake_color="blue", starting_coords=(-140,-300), head="north")
        for step in range(19):
            snake.move_one_step()
        snake.head_east()
        for step in range(3):
            snake.move_one_step()
        snake.head_south()
        for step in range(3):
            snake.move_one_step()
    
    def draw_a(self):
        snake = AnimatorSnake(no_of_units = 11, snake_color="yellow", starting_coords=(300,20), head="west")
        for step in range(17):
            snake.move_one_step()
        snake.head_north()
        for step in range(3):
            snake.move_one_step()
        snake.head_east()
        for step in range(3):
            snake.move_one_step()
        snake.head_south()
        for step in range(4):
            snake.move_one_step()
    
    def draw_k(self):
        snake = AnimatorSnake(no_of_units = 6, snake_color="green", starting_coords=(60,300), head="south")
        for step in range(14):
            snake.move_one_step()
        snake = AnimatorSnake(no_of_units = 5, snake_color="green", starting_coords=(100,300), head="south")
        for step in range(12):
            snake.move_one_step()
        snake.head_west()
        for step in range(2):
            snake.move_one_step()
        snake = AnimatorSnake(no_of_units = 2, snake_color="green", starting_coords=(120,-300), head="north")
        for step in range(18):
            snake.move_one_step()
    
    def draw_e(self):
        snake = AnimatorSnake(no_of_units = 12, snake_color="cyan", starting_coords=(300,20), head="west")
        for step in range(7):
            snake.move_one_step()
        snake.head_north()
        for step in range(3):
            snake.move_one_step()
        snake.head_east()
        for step in range(3):
            snake.move_one_step()
        snake.head_south()
        snake.move_one_step()

    def clear_screen(self):
        self.screen.clear()
        self.screen.bgcolor("black")


    def start_count(self):
        self.home()
        self.print_message("3")
        sleep(1)
        self.clear()
        self.print_message("2")
        sleep(1)
        self.clear()
        self.print_message("1")
        sleep(1)
        self.clear()

        

    def show_options(self,options):
        y = -100
        for option in options:
            self.penup()
            self.goto(-65, y)
            self.print_message(option, fontsize=30, alignment="left" )
            y -= 50


    def add_selector(self,x_coords=-80, y_coords = -55):
        self.x_coords=x_coords
        self.y_coords=y_coords
        self.selector = Selector((self.x_coords, self.y_coords))

    def select_below(self):
        if self.y_coords > -155:
            print("Select Down")
            self.selector.clear()
            self.add_selector(y_coords=self.y_coords-50)
    
    def select_up(self):
        if self.y_coords < -55:
            print("Select Up")
            self.selector.clear()
            self.add_selector(y_coords=self.y_coords+50)


    def select(self):
        if self.x_coords==-80 and self.y_coords==-55:
            self.selected_option = str(self.options[0]).lower()
        elif self.x_coords==-80 and self.y_coords==-105:
            self.selected_option = str(self.options[1]).lower()
        elif self.x_coords==-80 and self.y_coords==-155:
            self.selected_option = str(self.options[2]).lower()

    def select_options(self):
        self.selected_option=""
        self.screen.listen()
        self.screen.onkey(self.select_below, "Down")
        self.screen.onkey(self.select_up, "Up")
        self.screen.onkey(self.select, "space")
        while True:
            self.screen.update()
            if self.selected_option!="":
                return
        
    # def show_buttons(self):
    #     self.color("white")
    #     self.penup()
    #     self.goto(0, -100)
    #     self.print_message("Start", fontsize=30 )
    #     self.goto(0, -150)
    #     self.print_message("Settings", fontsize=30 )
    #     self.goto(0, -200)
    #     self.print_message("Help", fontsize=30 )
    #     self.x_coords=-80
    #     self.y_coords=-55
    #     for i in range(3):
    #         self.button_boundary = ButtonBoundary((self.x_coords, self.y_coords))
    #         self.y_coords -= 48
    #         print(self.y_coords)
    #     self.onclick(self.click_button)
    #     screen = AnimatorSnake()
    #     screen.screen.listen()
    #     screen.screen.exitonclick()

    # def click_button(self, x, y):
    #     if x > -80 and x < 80 and y < -55 and y > -7:
    #         print("button clicked!")