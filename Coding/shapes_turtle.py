import turtle
from turtle import *
t = Turtle()
s = Screen()
t.speed(0)

colors = ["lightblue","blue"]
for i in range(20):
    t.pencolor(colors[i%2])
    t.circle(120)
    t.right(20)
    t.fillcolor("lightblue")


# for i in range(3):
#     t.forward(300)
#     t.left(120)
    

    
