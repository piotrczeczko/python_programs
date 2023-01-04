from turtle import Turtle, Screen
import random

def move_forward(turtle_object):
    random_steps = random.randint(0,10)
    turtle_object.forward(random_steps)
    continue_race = check_the_winner(turtle_object)
    return continue_race


def check_the_winner(turtle_object):
    if turtle_object.xcor() > meta_lane:
        print(f"Turtle {turtle_object.color()[0]} won the race!")
        if user_bet == turtle_object.color()[0]:
            print("You won !!!")
            continue_race = False
        else:
            print("You lose :( ")
            continue_race = False
    return continue_race


#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
# def clear_screen():
#     #tim.goto(0,0)
#     #tim.clear()
#     tim.reset()



# screen.listen()
# screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)


is_race_on = False
meta_lane = 235
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(1, len(colors) +1 ):
    turtles.append(Turtle(shape="turtle"))
    turtles[i - 1].color(colors[i-1])
    turtles[i - 1].penup()
    turtles[i - 1].goto(x=-meta_lane, y=-170 + 50 * i)

if user_bet:
    is_race_on = True

while is_race_on:
    turtle_moving = random.choice(turtles)
    is_race_on = move_forward(turtle_moving)
    #print(turtle_moving)


#tim = Turtle(shape="turtle")
#tim.penup()
#tim.goto(x=-235,y=-180 )
# print(user_bet)
screen.exitonclick()
