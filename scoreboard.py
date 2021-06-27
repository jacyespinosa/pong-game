from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color('white')
        self.hideturtle()
        self.left_write_score()
        self.right_write_score()

    def left_write_score(self):
        self.penup()
        self.setposition(x=-100, y=270)
        self.pendown()
        self.write("PLAYER ONE: {}".format(self.left_score), align="center", font=("Times New Roman", 20, "normal"))

    def right_write_score(self):
        self.penup()
        self.setposition(x=100, y=270)
        self.pendown()
        self.write("PLAYER TWO: {}".format(self.right_score), align="center", font=("Times New Roman", 20, "normal"))

    def left_track_score(self):
        self.left_score += 1
        self.clear()
        self.left_write_score()
        self.right_write_score()

    def right_track_score(self):
        self.right_score += 1
        self.clear()
        self.right_write_score()
        self.left_write_score()

    def game_over(self, player):
        self.clear()
        self.penup()
        self.setposition(x=0, y=20)
        self.pendown()
        self.hideturtle()