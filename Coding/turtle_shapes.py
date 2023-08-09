# import turtle
# from turtle import *
# t = Turtle()
# s = Screen()
# t.shape("square")
# s.bgpic("spaceship_imgs/background.png")
# t.speed(10)
# for i in range(100):
#     t.color("white")
#     t.circle(i)
#     t.left(10)
#     t.forward(6)
    
# done()

import turtle
from turtle import *
s = Screen()
s.bgcolor("black")
def myshape():
    t = Turtle()
    colors = ["red","orange","yellow","lightblue","pink","purple"]
    t.speed(5)
    for i in range(360):
        t.pencolor(colors[i%6])
        t.forward(i)
        t.left(90)
        
        


        
        
myshape()

        