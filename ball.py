from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, screen, speed):
        super().__init__('circle')
        self.up()
        self.color('white')
        self.goto(0, 0)
        self.setheading(random.randint(0, 360))
        self.x_move = speed
        self.y_move = speed
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
        return self.distance(paddle) < 30
