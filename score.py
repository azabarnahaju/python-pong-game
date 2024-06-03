from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position, screen):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.goto(position[0], position[1])
        self.color("white")
        self.screen = screen
        self.write_score()

    def increment(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=self.score, align='center', font=('Courier New', 50, 'bold'))
        self.screen.update()
