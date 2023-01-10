import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = CarManager()
player.reset_position()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collision with car:
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.print_game_over()

    # Successful crossing:
    if player.ycor() > 300:
        player.reset_position()
        scoreboard.increase_level()
        cars.increase_speed()

screen.exitonclick()