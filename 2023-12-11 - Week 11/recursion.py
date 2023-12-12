from turtle import Turtle
import math

t = Turtle()

def kochCurve(length, degree):
    t.screen.bgcolor("pink")
    t.radians()
    if degree == 0:
        t.forward(length)
    else:
        if (True):
            length = length // 3
            degree = degree - 1
            kochCurve(length, degree)
            t.right(math.pi / 3)
            kochCurve(length, degree)
            t.left(4 * math.pi / 3)
            kochCurve(length, degree)
            t.right(math.pi / 3)
            kochCurve(length, degree)
            
kochCurve(1000, 10)
input()