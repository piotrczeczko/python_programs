import random
from turtle import Turtle
from random import randint
from variables import *
DISTANCE = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-round(SCREEN_WIDTH / 2) + DISTANCE,
                                  round(SCREEN_WIDTH / 2) - DISTANCE)
        random_y = random.randint(-round(SCREEN_WIDTH / 2) + DISTANCE,
                                  round(SCREEN_WIDTH / 2) - DISTANCE)
        self.goto(random_x, random_y)
