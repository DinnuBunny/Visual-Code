import turtle
col = ('red','yellow','green','cyan','pink','white','green','cyan','pink','white','yellow','red')
t = turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(25)

for i in range(150):
    t.color(col[i%6])
    t.forward(i*2)
    t.left(59)
    t.width(3)

turtle.done()