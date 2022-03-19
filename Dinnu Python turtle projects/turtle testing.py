import turtle
t = turtle.Turtle()
turtle.title("Testing")

screen = turtle.Screen()
screen.bgcolor('black')
t.color('white')

t.speed(10)
t.penup()
t.goto(-250,100)
t.pendown()

t.left(90)
t.forward(150)
t.right(90)
t.forward(2)
t.right(45)
t.forward(210)
t.left(45)
t.forward(2)
t.left(90)
t.forward(150)

t.color('black')
t.right(90)
t.forward(50)

t.color('white')
t.right(45)
t.forward(210)
t.right(180)
t.forward(105)
t.left(90)
t.forward(105)
t.right(180)
t.forward(210)

t.color('black')
t.right(45)
t.forward(50)

t.color('white')
t.forward(120)

t.right(180)
t.forward(60)

t.color('white')
t.left(90)
t.forward(150)
#t.color('black')





t.penup()
t.goto(-250,90)
t.pendown()


#W letter
t.color('white')
t.left(20)
t.forward(150)


t.left(145)
t.forward(90)

t.right(145)
t.forward(90)

t.left(140)
t.forward(150)


turtle.done()