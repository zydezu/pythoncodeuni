import turtle
from turtle import *
 
setup(500, 500)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
showturtle()
 
def up():
    tracer(1)
    turtle.forward(10)
    update()
 
def down():
    tracer(1)
    turtle.forward(-10)
    update()
 
def left():
    tracer(1)
    turtle.left(10)
    update()
 
def right():
    tracer(1)
    turtle.right(10)
    update()
    
def toggledraw():
    print(turtle.isdown())
    if (turtle.isdown()):
        turtle.penup()
    else:
        turtle.pendown()
 
onkeypress(up, 'Up')
onkeypress(down, 'Down')
onkeypress(left, 'Left')
onkeypress(right, 'Right')
onkeypress(toggledraw, 'space')
onscreenclick(turtle.goto)
listen()
 
turtle.screen.mainloop()