import turtle


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

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        # erase the turtle pathway
        self.turtle.penup()
        self.turtle.goto(0, 0)
        # init move vector
        self.dx = 1
        self.dy = 1

    def move(self):
        self.turtle.setx(self.turtle.xcor()+self.dx)
        self.turtle.sety(self.turtle.ycor()+self.dy)

    def colision(self):
        # up and down (height=600)
        if self.turtle.ycor() > 280:
            self.turtle.sety(280)
            self.dy *= -1
        if self.turtle.ycor() < -280:
            self.turtle.sety(-280)
            self.dy *= -1

        # left and right (width=800)
        if self.turtle.xcor() > 380:
            self.turtle.setx(380)
            self.dx *= -1
        if self.turtle.xcor() < -380:
            self.turtle.setx(-380)
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
    ball = Ball()
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
