from turtle import Turtle
from border import WIDTH, HEIGHT


X = WIDTH
Y = HEIGHT

SCORE_X_POSITION = 0
SCORE_Y_POSITION = HEIGHT / 2 + 20

GAME_OVER_POSITION = 0

INSTRUCTION_Y_POSITION = - HEIGHT / 2 + 20
INSTRUCTION_X_POSITION = (- HEIGHT / 2) + 150

ALIGN = "center"
FONT = ("arial", 16)
S_COLOR = "white"
SPEED = "fastest"
GAME_OVER_TEXT = "GAME OVER"
FILE_NAME = "snake_data.txt"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.text = None
        self.top = 0
        self.count = 0
        self.retrieve_score()
        self.penup()
        self.color(S_COLOR)
        self.hideturtle()
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        """Changes the text in the score"""
        self.text = f"Score: {self.count} - Highest score: {self.top}"
        self.write(self.text, False, ALIGN, FONT)

    def reset_instructions(self):
        """Shows on screen options for the user"""
        self.goto(INSTRUCTION_X_POSITION, INSTRUCTION_Y_POSITION)
        self.text = "New try: bar\nQuit: q"
        self.write(self.text, align=ALIGN, font=FONT)

    def update(self):
        """Updates the score of the snake once it eats"""
        self.count += 1
        self.clear()
        self.refresh()

    def show_game_over(self):
        """Displays in the center of the screen game over text"""

        self.penup()
        self.hideturtle()
        self.goto(GAME_OVER_POSITION, GAME_OVER_POSITION)
        self.color("red")
        self.write(GAME_OVER_TEXT, align=ALIGN, font=FONT)

    def game_over(self):
        """Displays text and checks the user score to update the board"""
        self.show_game_over()
        self.is_highest()
        self.reset_instructions()

    def is_highest(self):
        """Saves highest score to data if True"""

        if self.count > self.top:
            self.save_top()

    def retrieve_score(self):
        """Retrieves highest score from FILE_NAME"""

        try:
            with open(FILE_NAME, "r") as saved:
                str_score = saved.read()
                int_score = int(str_score)
        except (FileNotFoundError, ValueError):
            print("Some error bro")
        else:
            self.top = int_score

    def save_top(self):
        """Saves score to FILE_NAME"""

        with open(FILE_NAME, "w") as saved:
            score = str(self.count)
            saved.write(score)
            print("data saved, allegedly")

