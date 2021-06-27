from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')


game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if scoreboard.left_score == 2:
        scoreboard.game_over(scoreboard.left_score)
        scoreboard.write("PLAYER 1 WINS!!!", align="center", font=("Times New Roman", 50, "normal"))
        game_over = True
    elif scoreboard.right_score == 2:
        scoreboard.game_over(scoreboard.right_score)
        scoreboard.write("PLAYER 2 WINS!!!", align="center", font=("Times New Roman", 50, "normal"))
        game_over = True

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.other_bounce()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_track_score()
    elif ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_track_score()


screen.listen()
screen.exitonclick()
