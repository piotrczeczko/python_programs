from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
FONT_OVER = ("Arial", 30, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

