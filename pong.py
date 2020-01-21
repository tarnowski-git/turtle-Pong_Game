import turtle
import math

from turtle import Turtle, Screen


class Pencil():

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=10, stretch_len=1)
        self.turtle.penup()
        self.turtle.goto(0, 250)
        self.turtle.write("Player A: 0 | Player B: 0",
                          align="center", font=("Arial", 30))

    def display(self, ponits_A, points_B):
        self.turtle.clear()
        self.turtle.write("Player A: {} | Player B: {}".format(
            ponits_A, points_B), align="center", font=("Arial", 30))


class Paddle():

    def __init__(self, position):
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=10, stretch_len=1)
        # erase the turtle pathway
        self.turtle.penup()
        self.turtle.goto(position, 0)

    def go_up(self):
        y = self.turtle.ycor()
        y += 30
        if y < 250:
            self.turtle.sety(y)

    def go_down(self):
        y = self.turtle.ycor()
        y -= 30
        if y > -250:
            self.turtle.sety(y)


class Ball():

    def __init__(self, a, b, pencil):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        # erase the turtle pathway
        self.turtle.penup()
        self.turtle.goto(0, 0)
        # init move vector
        self.dx = 0.5
        self.dy = 0.5
        self.a = a
        self.b = b
        self.pencil = pencil
        self.ponits_A = 0
        self.ponits_B = 0

    def move(self):
        self.turtle.setx(self.turtle.xcor()+self.dx)
        self.turtle.sety(self.turtle.ycor()+self.dy)

    def colision(self):
        # up and down (height=600)
        if self.turtle.ycor() > 290:
            self.turtle.sety(290)
            self.dy *= -1

        if self.turtle.ycor() < -290:
            self.turtle.sety(-290)
            self.dy *= -1

        # left and right (width=800)
        if self.turtle.xcor() > 390:
            self.turtle.setx(390)
            self.dx *= -1
            self.ponits_A += 1
            self.pencil.display(self.ponits_A, self.ponits_B)

        if self.turtle.xcor() < -390:
            self.turtle.setx(-390)
            self.dx *= -1
            self.ponits_B += 1
            self.pencil.display(self.ponits_A, self.ponits_B)

        # paddles
        if self.turtle.xcor() < -330 and math.fabs(self.turtle.ycor() - self.a.turtle.ycor()) < 50:
            self.turtle.goto(-320, self.turtle.ycor())
            self.dx *= -1

        if self.turtle.xcor() > 330 and math.fabs(self.turtle.ycor() - self.b.turtle.ycor()) < 50:
            self.turtle.goto(320, self.turtle.ycor())
            self.dx *= -1


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
        self.paddle_1 = Paddle(-350)
        self.paddle_2 = Paddle(350)
        self.score = Pencil()
        self.ball = Ball(self.paddle_1, self.paddle_2, self.score)
        # Create keyboard bindings
        self.screen.listen()
        self.screen.onkeypress(self.paddle_1.go_up, "w")
        self.screen.onkeypress(self.paddle_1.go_down, "s")
        self.screen.onkeypress(self.paddle_2.go_up, "Up")
        self.screen.onkeypress(self.paddle_2.go_down, "Down")

    def run(self):
        """Make the game loop a function."""

        while True:
            self.screen.update()    # Display the screen.
            self.ball.move()
            self.ball.colision()


if __name__ == "__main__":
    Game().run()
