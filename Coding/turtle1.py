import turtle
from turtle import *

t = Turtle()
s = Screen()
t.shape("turtle")
s.bgcolor("lightblue")
s.title("Turtle Project 1")
t.color("black","blue")
t.speed(1)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
    
t.penup()
t.right(90)
t.forward(100)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.right(90)
t.forward(50)
t.pendown()


for i in range(4):
    t.forward(100)
    t.left(90)


t.end_fill()


done()

