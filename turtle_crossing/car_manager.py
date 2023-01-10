import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # generate a car
    def create_car(self):
        #for i in range(random.randint(0, 5)):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for idx, car in enumerate(self.all_cars):
            car.forward(self.car_speed)
            if car.xcor() < -310:
                self.all_cars.pop(idx)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT






