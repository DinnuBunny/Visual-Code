import turtle
t = turtle.Turtle()
turtle.title("Heart Shape")

screen = turtle.Screen()
screen.bgcolor("black")

t.speed(5)
t.penup()
t.goto(0,-100)
t.pendown()

t.color("orange")
t.begin_fill()
t.fillcolor('red')
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.hideturtle()
turtle.done()
