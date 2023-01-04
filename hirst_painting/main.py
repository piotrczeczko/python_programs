# import colorgram
#
# color_pallet = []
# colors = colorgram.extract('image.jpg', 21)
# for color in colors:
#     color_pallet.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(color_pallet)
import random
import random as r
from turtle import Turtle, Screen
from math import sqrt

color_list = [(236, 230, 233), (232, 238, 234), (223, 232, 237), (236, 34, 109), (152, 25, 64), (240, 74, 34), (7, 148, 94), (237, 167, 40), (182, 158, 45), (44, 191, 232), (27, 125, 192), (126, 193, 75), (83, 25, 86), (253, 223, 0), (245, 220, 43), (186, 38, 103), (61, 174, 100), (213, 59, 24), (164, 24, 21), (209, 130, 166)]
nb_dots_in_line = 10
nb_lines = 10
dot_size = 20
dot_space = 50

tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()


def draw_dot():
    tim.dot(dot_size, random.choice(color_list))


def draw_line_dots():
    for i in range(0, nb_dots_in_line):
        draw_dot()
        tim.forward(dot_space)


def go_to_new_line():
    tim.setheading(90)
    tim.forward(dot_space)
    tim.setheading(180)
    tim.forward(dot_space * nb_dots_in_line)
    tim.setheading(0)


def set_window_size():
    x = (dot_space * nb_dots_in_line) + round((dot_space * nb_dots_in_line) / 10)
    y = (dot_space * nb_lines) + round((dot_space * nb_lines) / 10)
    return x, y


def go_to_start():
    tim.setx(-round((nb_dots_in_line * dot_space) / 2) + dot_space)
    tim.sety(-round((nb_lines * dot_space) / 2) + dot_space)


def draw_picture():
    for i in range(0, nb_lines):
        draw_line_dots()
        go_to_new_line()

##############################################################
screen = Screen()
window_size_x, window_size_y = set_window_size()
screen.screensize(window_size_x,window_size_y)
screen.colormode(255)
go_to_start()
##############################################################
#screen.screensize(200, 150)

draw_picture()
screen.exitonclick()


#10 x 10
#20 ---50--- 20