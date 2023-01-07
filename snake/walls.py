from turtle import Turtle

class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(-295, 295)
        self.pendown()
        self.hideturtle()
        self.draw_walls()

    def draw_walls(self):
        for side_number in range(4):
            self.forward(585)
            self.right(90)

