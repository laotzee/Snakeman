
import border, food, score, snake
import turtle

NEGATIVE_BORDER = (border.X[0], border.Y[0])
POSITIVE_BORDER = (border.X[1], border.Y[1])

BG_COLOR = "black"
GAME_NAME = "Snake Game"
game_on = True
run = True
print(type(turtle))
print(type(turtle.Screen))

class SnakeScreen(turtle._Screen):

    def __init__(self):
        super().__init__()
        self.setup(border.WIDTH, border.HEIGHT)
        self.title(GAME_NAME)
        self.bgcolor(BG_COLOR)
        self.tracer(0)
        self.game_on = True
        self.quit_game = False
        self.snake = snake.Snake(self)
        self.food = food.Food()
        self.score = score.Score()
        self.border = border.Border()


    def run(self):
        """Initiates a game"""

        while self.game_on:

            if self.snake.is_game_over(NEGATIVE_BORDER, POSITIVE_BORDER,
                                       self.score.count):
                self.game_on = False
                self.score.game_over()

            elif self.snake.head.distance(self.food) < food.PART_SIZE:
                self.snake.increase_body()
                self.food.refresh()
                self.score.update()


