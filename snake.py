import turtle as t
from time import sleep


SNAKE_COLOR = "white"
STARTER_BODY = 2
PART_SIZE = 10
PART_DISTANCE = PART_SIZE * 5
DIRECTION = [0, 90, 180, 270]
SPEED = 0.2
SHAPE = "square"
SIZE = "auto"
MV = "fastest"

class Snake:
    """Models the behaviour of a snake"""

    def __init__(self, screen):
        self.screen = screen
        self.snake_body = []
        for i in range(STARTER_BODY):
            self.create_part()
        self.head = self.snake_body[0]


    def create_part(self):
        """Creates a part for the body of a snake"""
        part = t.Turtle()
        part.shape(SHAPE)
        part.pencolor(SNAKE_COLOR)
        part.penup()
        part.pensize(PART_SIZE)
        part.resizemode(SIZE)
        part.speed(MV)
        self.snake_body.append(part)

    def erase_body(self):

        for bit in self.snake_body:
            bit.reset()
        self.snake_body = []

    def increase_body(self):
        """Adds a part to the tail of a snake"""
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.create_part()
        self.snake_body[-1].teleport(x, y)

    def turn_up(self):
        """Turns the head of the snake north"""
        self.head.seth(90)

    def turn_down(self):
        """Turns the head of the snake south"""
        self.head.seth(270)

    def turn_left(self):
        """Turns the head of the snake west"""
        self.head.seth(180)

    def turn_right(self):
        """Turns the head of the snake east"""
        self.head.seth(0)

    def map_keys(self):
        """Maps the keys 'wasd' and vim keys for snake's movement"""

        # VIM (HJKL)
        self.screen.onkey(key="l", fun=self.turn_right)
        self.screen.onkey(key="k", fun=self.turn_up)
        self.screen.onkey(key="j", fun=self.turn_down)
        self.screen.onkey(key="h", fun=self.turn_left)

        # WASD
        self.screen.onkey(key="w", fun=self.turn_up)
        self.screen.onkey(key="a", fun=self.turn_left)
        self.screen.onkey(key="s", fun=self.turn_down)
        self.screen.onkey(key="d", fun=self.turn_right)

    def restrict_movement(self):
        """Restricts the movement of the snake depending on its direction"""

        d = self.head.heading()

        if d == DIRECTION[0]:
            self.screen.onkey(key="a", fun=None)
            self.screen.onkey(key="h", fun=None)
        elif d == DIRECTION[1]:
            self.screen.onkey(key="s", fun=None)
            self.screen.onkey(key="j", fun=None)
        elif d == DIRECTION[2]:
            self.screen.onkey(key="d", fun=None)
            self.screen.onkey(key="l", fun=None)
        else:
            self.screen.onkey(key="k", fun=None)
            self.screen.onkey(key="w", fun=None)

    def move_head(self):
        """Moves head in the direction the user commands it to"""
        self.map_keys()
        self.restrict_movement()
        self.screen.listen()
        print(self.head.pos())
        self.head.fd(PART_DISTANCE)

    def move(self):
        """Moves the entire body of the snake"""

        total_snake_body = len(self.snake_body) - 1

        for part in range(total_snake_body, -1, -1):
            if part == 0:
                self.move_head()
            else:
                next_part = self.snake_body[part - 1]
                next_pos = next_part.pos()
                self.snake_body[part].goto(next_pos)
        sleep(SPEED)
        #! I should take out sleep and place it elsewhere

    def self_collision(self, score):
        """Detects if snake collides with itself"""

        x_head = self.head.xcor()
        y_head = self.head.ycor()

        for i in range(1, len(self.snake_body)):
            x_part = self.snake_body[i].xcor()
            y_part = self.snake_body[i].ycor()
            if x_part == x_head and y_part == y_head and score > 3:
                print("It was meeee!!! self collision")
                return True

    def on_border(self, n, p):
        """Given borders, detects if snake collided has collided with them"""

        x_head = self.head.xcor()
        y_head = self.head.ycor()

        if x_head <= n[0] or x_head >= p[0]:
            return True
        elif y_head <= n[1] or y_head >= p[1]:
            return True
        else:
            return False


    def is_game_over(self, negative_borders, positive_borders, score):
        """Returns true if the snake has collided with walls or itself"""

        return self.on_border(negative_borders,
                              positive_borders) or self.self_collision(score)







