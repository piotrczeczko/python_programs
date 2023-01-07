from turtle import Turtle

SNAKE_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            position_x = -i * SNAKE_MOVE_DISTANCE
            position_y = 0
            self.add_segment((position_x,position_y))

    def add_segment(self, position):
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[-1].color("white")
        self.snake_body[-1].penup()
        #self.snake_body[-1].speed(3)
        self.snake_body[-1].goto(position)

    def extend(self):
        # add new segment to the snake
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(SNAKE_MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
