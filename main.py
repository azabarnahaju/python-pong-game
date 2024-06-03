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
from score import ScoreBoard

game_screen = GameScreen()

player_1 = Paddle(game_screen.screen, (-480, 0), 'w', 's', 'Player 1')
player_2 = Paddle(game_screen.screen, (480, 0), 'Up', 'Down', 'Player 2')
player_1_score = ScoreBoard((-150, 200), game_screen.screen)
player_2_score = ScoreBoard((150, 200), game_screen.screen)

ball = Ball(game_screen.screen)
winner = None

while winner is None:
    ball.move()

    if ball.is_hitting_paddle(player_1) or ball.is_hitting_paddle(player_2):
        ball.bounce_off_paddle()

    if ball.is_out_of_bounds():
        if ball.xcor() < -450:
            player_2_score.increment()
        else:
            player_1_score.increment()
        ball.respawn()

    if player_1_score.score == 10:
        winner = player_1
    elif player_2_score.score == 10:
        winner = player_2

game_screen.game_over(winner.name)
game_screen.screen.exitonclick()
