import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(9999)
sidelength = 100
rotate = 90
def square(x,y):
   for i in range(4):
    t.forward(x)
    t.left(y)
def AddSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
AddSquares(400)