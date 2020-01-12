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


def bind(window, a, b):
    window.listen()
    window.onkeypress(a.go_up, "w")
    window.onkeypress(a.go_down, "s")

    window.onkeypress(b.go_up, "Up")
    window.onkeypress(b.go_down, "Down")


def game(window):
    a = Paddle(350)
    b = Paddle(-350)
    bind(window, a, b)
    while True:
        window.update()


def main():
    window = turtle.Screen()
    setup_window(window)
    game(window)


main()
