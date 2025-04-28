
import snake as s
import food as f
import score as c
import border as b
import turtle as t


WIDTH = b.WIDTH
HEIGHT = b.HEIGHT
NEGATIVE_BORDER = (b.X[0], b.Y[0])
POSITIVE_BORDER = (b.X[1], b.Y[1])
BG_COLOR = "black"
GAME_NAME = "Snake Game"
colors = ["red", "green", "blue"]
game_on = True
quit = False
reset = True

current_screen = None
current_border = None
current_snake = None
current_food = None
current_score = None

def print_on_command(word):
    print(word)

def hear_options():

    global screen

    screen.onkey(key="space", fun=next_game)
    screen.onkey(key="q", fun=quit_game)

def desactivate_option():

    global screen

    screen.onkey(key="space", fun=None)
    screen.onkey(key="q", fun=None)

def next_game():

    global game_on
    global reset

    reset = True
    game_on = True
    screen.reset()


def quit_game():

    screen.bye()

screen = t.Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.title(GAME_NAME)
screen.bgcolor(BG_COLOR)


while not quit:

    if reset:
        current_border = b.Border()
        current_snake = s.Snake(screen)
        current_food = f.Food()
        current_score = c.Score()
        reset = False

    while game_on:

        screen.update()
        current_snake.move()

        if current_snake.is_game_over(NEGATIVE_BORDER, POSITIVE_BORDER,
                                 current_score.count):
            current_score.game_over()
            game_on = False
            hear_options()

        elif current_snake.head.distance(current_food) < f.PART_SIZE:
            current_snake.increase_body()
            current_food.refresh()
            current_score.update()

    screen.update()


screen.exitonclick()

