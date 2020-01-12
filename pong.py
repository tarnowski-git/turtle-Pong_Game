import turtle
import math


def setup_window(window):
    window.title("Pong Game")
    window.setup(width=800, height=600)
    # accelerate time program
    window.tracer(0)
    window.colormode(255)
    window.bgcolor("green")


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

    def __init__(self, a, b):
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
        if self.turtle.xcor() < -390:
            self.turtle.setx(-390)
            self.dx *= -1

        # paddles
        if self.turtle.xcor() < -330 and math.fabs(self.turtle.ycor() - self.a.turtle.ycor()) < 50:
            self.turtle.goto(-320, self.turtle.ycor())
            self.dx *= -1

        if self.turtle.xcor() > 330 and math.fabs(self.turtle.ycor() - self.b.turtle.ycor()) < 50:
            self.turtle.goto(320, self.turtle.ycor())
            self.dx *= -1


def bind(window, a, b):
    window.listen()
    window.onkeypress(a.go_up, "w")
    window.onkeypress(a.go_down, "s")
    window.onkeypress(b.go_up, "Up")
    window.onkeypress(b.go_down, "Down")


def game(window):
    a = Paddle(-350)
    b = Paddle(350)
    ball = Ball(a, b)
    bind(window, a, b)
    while True:
        window.update()
        ball.move()
        ball.colision()


def main():
    window = turtle.Screen()
    setup_window(window)
    game(window)


main()
