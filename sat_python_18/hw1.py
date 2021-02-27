import turtle
import time

t=turtle.Pen()
#--------------
t.pencolor('red')
turtle.bgcolor('black')

t.penup()
t.left(90)
t.forward(100)
t.pendown()

t.color('#FF0066','#00FFC1')
t.begin_fill()
t.circle(10)
t.end_fill()

#-----------------
time.sleep(100)

