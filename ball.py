from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__('circle')
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.goto(0, 0)
        self.speed(1)
        self.setheading(random.randint(0, 360))
        self.screen = screen
        self.screen.update()

    def move(self):
        if self.is_hitting_wall():
            self.bounce()
        self.fd(1)
        self.screen.update()

    def is_hitting_wall(self):
        return self.ycor()-5 <= -295 or self.ycor() + 5 >= 295

    def bounce(self):
        curr_heading = self.heading()
        if curr_heading < 90:
            new_heading = 270 + (90 - curr_heading)
        elif curr_heading < 180:
            new_heading = 270 - (curr_heading - 90)
        elif curr_heading < 270:
            new_heading = 90 + (270 - curr_heading)
        elif curr_heading < 360:
            new_heading = 90 - (curr_heading - 270)
        self.setheading(new_heading)

