from turtle import Turtle, Screen
from math import fabs


def is_collision(obj_1, obj_2):
    """Global function.
    It mesasure the absolute distance value on Cartesian coordinate system.
    """

    if isinstance(obj_1, Turtle) and isinstance(obj_2, Turtle):
        distance_x = fabs(obj_1.xcor() - obj_2.xcor())
        distance_y = fabs(obj_1.ycor() - obj_2.ycor())

        if distance_x == 20 and distance_y < 70:
            # print("collision {} {}".format(distance_x, distance_y))
            return True
        else:
            return False


class Paddle(Turtle):

    def __init__(self, xPos=0):
        Turtle.__init__(self)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()    # penup befor moving
        self.goto(xPos, 0)
        self.paddle_speed = 30

    def go_up(self):
        y = self.ycor()
        y += self.paddle_speed
        if y < 230:
            self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= self.paddle_speed
        if y > -230:
            self.sety(y)


class Ball(Turtle):

    def __init__(self, xVel=1.0, yVel=1.0):
        Turtle.__init__(self)
        self.color("red")
        self.shape("circle")
        self.penup()    # penup befor moving
        self.goto(0, 0)
        # init move vector
        self.dx = xVel
        self.dy = yVel
        self.ponits_A = 0
        self.ponits_B = 0

    def move(self):
        """Make move the ball"""
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_off(self):
        """Function take ball bounce off a paddle"""
        if self.xcor() <= -330:
            self.goto(-320, self.ycor())
            self.dx *= -1

        if self.xcor() >= 330:
            self.goto(320, self.ycor())
            self.dx *= -1

    def check_collision(self):
        """Function check if ball touch the border."""
        # up and down (height=600)
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

        # left and right (width=800)
        if self.xcor() > 390:
            self.setx(390)
            self.dx *= -1

        if self.xcor() < -390:
            self.setx(-390)
            self.dx *= -1


class Score(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        # initial variables
        self.points_A = 0
        self.points_B = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Player A: {} | Player B: {}".format(
            self.points_A, self.points_B), align="center", font=("Arial", 30))

    def add_score(self, points_A, points_B):
        self.points_A += points_A
        self.points_B += points_B
        self.update_score()


class Game():
    """Make the game loop into a class.
    Responsible for drawing and updating all our objects"""

    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.bgcolor("green")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong Game")
        # accelerate time program
        self.screen.tracer(0)
        self.screen.colormode(255)

        # initial objects
        self.paddle_left = Paddle(-350)
        self.paddle_right = Paddle(350)
        self.score = Score()
        self.ball = Ball(0.5, 0.5)

        # Create keyboard bindings
        self.screen.listen()
        self.screen.onkeypress(self.paddle_left.go_up, "w")
        self.screen.onkeypress(self.paddle_left.go_down, "s")
        self.screen.onkeypress(self.paddle_right.go_up, "Up")
        self.screen.onkeypress(self.paddle_right.go_down, "Down")

    def run(self):
        """Make the game loop a function."""

        while True:
            # move the ball
            self.ball.move()

            # checking the left border
            if self.ball.xcor() < -390:
                # add score for player A
                self.score.add_score(0, 1)

            # checking the right border
            if self.ball.xcor() > 390:
                # add score for player B
                self.score.add_score(1, 0)

            self.ball.check_collision()

            # checking collision between ball and left paddle
            if is_collision(self.paddle_left, self.ball):
                self.ball.bounce_off()

            # checking collision between ball and right paddle
            if is_collision(self.paddle_right, self.ball):
                self.ball.bounce_off()

            # Display the screen.
            self.screen.update()


if __name__ == "__main__":
    Game().run()
