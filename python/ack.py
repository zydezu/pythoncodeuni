import turtle

game: bool = True

win = turtle.Screen()
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# default value at start
paddle_a.move_up = False
paddle_a.move_down = False

# Functions
def paddle_a_up_start():
    paddle_a.move_up = True

def paddle_a_up_end():
    paddle_a.move_up = False
    
def paddle_a_down_start():
    paddle_a.move_down = True

def paddle_a_down_end():
    paddle_a.move_down = False


def paddle_b_up():
    if paddle_b.ycor() + 70 < 300:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() - 70 > -300:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# Keyboard binding
win.listen()

win.onkeypress(paddle_a_up_start, "w")
win.onkeyrelease(paddle_a_up_end, "w")

win.onkeypress(paddle_a_up_start, "W")
win.onkeyrelease(paddle_a_up_end, "W")

win.onkeypress(paddle_a_down_start, "s")
win.onkeyrelease(paddle_a_down_end, "s")

win.onkeypress(paddle_a_down_start, "S")
win.onkeyrelease(paddle_a_down_end, "S")


win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


while game:
    if paddle_a.move_up:
        if paddle_a.ycor() + 70 < 300:
            y = paddle_a.ycor()
            y += 2
            paddle_a.sety(y)

    if paddle_a.move_down:
        if paddle_a.ycor() - 70 > -300:
            y = paddle_a.ycor()
            y -= 2
            paddle_a.sety(y)

    win.update()
