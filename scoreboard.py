from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("arial", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("arial", 70, "normal"))

    def left_goal(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def right_goal(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()