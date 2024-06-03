from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__('circle')
        self.up()
        self.color('white')
        self.goto(0, 0)
        self.x_move = 1
        self.y_move = 1
        self.screen = screen
        self.screen.update()

    def move(self):
        if self.is_hitting_wall():
            self.bounce_off_wall()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        self.screen.update()

    def is_hitting_wall(self):
        return self.ycor()-5 <= -295 or self.ycor() + 5 >= 295

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1

    def is_hitting_paddle(self, paddle):
        return self.distance(paddle) < 30 and (self.xcor() > 340 or self.xcor() < -340)

    def is_out_of_bounds(self):
        return self.xcor() > 495 or self.xcor() < -495

    def respawn(self):
        self.x_move = 1
        self.y_move = 1
        self.goto(0, 0)
        self.screen.update()
