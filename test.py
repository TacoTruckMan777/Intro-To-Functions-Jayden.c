import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
t.speed(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
for i in range(6009999999999999):
    square(200)
    t.right(0.1)