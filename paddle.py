from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen, starting_pos, control_up, control_down, name):
        super().__init__('square')
        self.name = name
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.color('white')
        self.goto(starting_pos[0], starting_pos[1])
        self.speed('fastest')
        screen.onkeypress(key=control_up, fun=self.__go_up)
        screen.onkeypress(key=control_down, fun=self.__go_down)
        screen.update()
        self.screen = screen

    def __go_up(self):
        if not self.is_hitting_wall_top():
            curr_y = self.ycor()
            self.sety(curr_y + 20)
        self.screen.update()

    def __go_down(self):
        if not self.is_hitting_wall_bottom():
            curr_y = self.ycor()
            self.sety(curr_y - 20)
        self.screen.update()

    def is_hitting_wall_top(self):
        return self.distance((-480, 300)) < 50 or self.distance((480, 300)) < 50

    def is_hitting_wall_bottom(self):
        return self.distance((-480, -300)) < 50 or self.distance((480, -300)) < 50


