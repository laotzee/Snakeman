from turtle import Turtle

WIDTH = 1000
HEIGHT = 1000
BODY_SIZE = 10
COLOR = "white"
SIZE = "auto"
MV = "fastest"

X = (-WIDTH/2, WIDTH/2)
Y = (-HEIGHT/2, HEIGHT/2)

START_X = X[0]
START_Y = Y[0]


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(BODY_SIZE)
        self.resizemode(SIZE)
        self.speed(MV)
        self.color(COLOR)
        self.penup()
        self.goto(START_X, START_Y)
        self.draw()

    def draw(self):
        self.pendown()
        for i in range(4):
           self.fd(WIDTH)
           self.left(90)
