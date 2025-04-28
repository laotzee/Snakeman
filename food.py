from turtle import Turtle
from snake import PART_SIZE
from random import choice

BODY_SIZE = PART_SIZE
VALID_LOCATIONS = [-450, -400, -350, -300, -250, -200, -150, -100, -50,
                   0, 50, 100, 150, 200, 250, 300, 350, 400, 450]

SHAPE = "circle"
COLOR = "red"
SIZE = "auto"
SPEED = "fastest"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.pencolor(COLOR)
        self.pensize(PART_SIZE)
        self.resizemode(SIZE)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        x = choice(VALID_LOCATIONS)
        y = choice(VALID_LOCATIONS)
        self.goto(x, y)








