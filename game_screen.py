from turtle import Screen, Turtle


class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.__initial_setup()

    def __initial_setup(self):
        self.screen.tracer(0)
        self.screen.setup(width=1000, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong Game')
        self.__create_half_line()
        self.screen.listen()
        self.screen.update()
        self.__create_screen_message()

    @staticmethod
    def __create_half_line():
        half_line = Turtle('square')
        half_line.shapesize(stretch_wid=0.5, stretch_len=0.1)
        half_line.color('white')
        half_line.penup()
        x, y = 0, 280
        while y >= -275:
            half_line.goto(x, y)
            half_line.stamp()
            y -= 20

    def __create_screen_message(self):
        self.message = Turtle()
        self.message.up()
        self.message.ht()
        self.message.color('yellow')

    def game_over(self, winner):
        self.message.goto(0, 0)
        self.message.write(arg='GAME OVER!', align='center', font=('Courier New', 30, 'bold'))
        self.message.goto(0, -40)
        self.message.write(arg=f'{winner} has won!', align='center', font=('Courier New', 30, 'bold'))
