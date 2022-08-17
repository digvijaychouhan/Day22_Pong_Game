from turtle import Turtle

SHIFT = 20
COORDINATES = [(280, 0), (-280, 0)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + SHIFT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SHIFT
        self.goto(self.xcor(), new_y)

