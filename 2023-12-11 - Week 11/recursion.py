from turtle import Turtle
import math
import random


colors = ["red", "yellow", "orange",
           "pink", "blue", "green"]

t = Turtle()

def kochCurve(length, degree):
    t.screen.bgcolor(random.choice(colors))
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


def triangle(size):
    for angle in [-120, -120, 0]:
        koch(t, order, size)
        t.left(angle)


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size // 3)
        t.left(60)
        koch(t, order - 1, size // 3)
        t.right(120)
        koch(t, order - 1, size // 3)
        t.left(60)
        koch(t, order - 1, size // 3)
            
t.pensize(5)
t.penup()
t.setpos(-450, 250)
t.pendown()
t.speed(0)

size = 900
order = 4
triangle(size)


# kochCurve(5, 10)
input()