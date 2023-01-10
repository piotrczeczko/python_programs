from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.print_score()


    def print_score(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 18, "normal"))

    def increase_level(self):
        self.level += 1
        self.print_score()


    def print_game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"Game Over", align="center", font=("Courier", 18, "normal"))

