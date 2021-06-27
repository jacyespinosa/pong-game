from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.penup()
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        self.y_move *= -1

    def other_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.other_bounce()
