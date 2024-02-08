from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = 5
        self.update_scoreboard()

# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()
#
    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 230)
        self.write(f"Level {self.level}", align="center", font=FONT)
#         self.goto(100, 190)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
#

    def point(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(180, 230)
        self.write(f"Lives: {self.lives}", align="center", font=FONT)

    def deduct_life(self):
        self.lives -= 1
        self.update_lives()
