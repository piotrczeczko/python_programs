from turtle import Turtle

WIDTH = 20
HEIGHT = 100
X_POS = 350
Y_POS = 40
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.paddle_body = []
        self.create_paddle()
        self.head = self.paddle_body[0]
        self.tail = self.paddle_body[4]
        #self.head = self.snake_body[0]

    def create_paddle(self):
        for i in range(5):
            position_x = X_POS
            position_y = Y_POS - (i * WIDTH)
            self.add_segment((position_x, position_y))

    def add_segment(self, position):
        self.paddle_body.append(Turtle(shape="square"))
        self.paddle_body[-1].color("white")
        self.paddle_body[-1].penup()
        self.paddle_body[-1].goto(position)

    def move_up(self):
        for seg_num in range(len(self.paddle_body)-1,0, -1):
            new_x = self.paddle_body[seg_num-1].xcor()
            new_y = self.paddle_body[seg_num-1].ycor()
            self.paddle_body[seg_num].goto(new_x, new_y)
        self.head.forward(20)


    def move_down(self):
        for seg_num in range(0,len(self.paddle_body)-1):
            new_x = self.paddle_body[seg_num+1].xcor()
            new_y = self.paddle_body[seg_num+1].ycor()
            self.paddle_body[seg_num].goto(new_x, new_y)
        self.tail.forward(20)

    def up(self):
        self.head.setheading(UP)
        self.move_up()

    def down(self):
        self.tail.setheading(DOWN)
        self.move_down()
