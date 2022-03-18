from turtle import *

bgcolor('black')
speed(0.001)
hideturtle()

for i in range(1200):
    color('red')
    circle(i)
    color('green')
    circle(i * 0.8)
    right(5)
    forward(4)
done()