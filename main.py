# TODO: Create the screen
# TODO: Create and move a paddle
# TODO: Create another paddle
# TODO: Create the ball and make it move
# TODO: Detect collision with wall and bounce
# TODO: Detect collision with pallet
# TODO: Detect when paddle misses
# TODO: Keep score

from ball import Ball
from game_screen import GameScreen
from paddle import Paddle

game_screen = GameScreen()

player_1 = Paddle(game_screen.screen, (-480, 0), 'w', 's')
player_2 = Paddle(game_screen.screen, (480, 0), 'Up', 'Down')
speed = 1
ball = Ball(game_screen.screen, speed)
is_game_on = True

while is_game_on:
    ball.move()
    if ball.is_hitting_paddle(player_1) or ball.is_hitting_paddle(player_2):
        ball.bounce_off_paddle()

game_screen.screen.exitonclick()
