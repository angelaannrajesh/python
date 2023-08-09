import turtle
import math
import time
import random
from turtle import *

delay = 0.1
score = 0
highscore = 0
bodies = []

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width= 600, height= 600)
# creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("green")
head.penup()
head.goto(0,0)
head.direction ="stop"
# making the food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.fillcolor("yellow")
food.penup()
food.goto(0,200)
#scoreboard
sb = turtle.Turtle()
sb.color("white")
sb.penup()
sb.goto(-250,250)
sb.write("Score:0, Highscore:0")

    

def MoveUp():
    if head.direction != "down":
        head.direction = "up"

def MoveDown():
    if head.direction != "up":
        head.direction = "down"

def MoveLeft():
    if head.direction != "right":
        head.direction = "left"

def MoveRight():
    if head.direction != "left":
        head.direction = "right"  
        
def MoveStop():
    head.direction = "stop"  
    
def Move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        

    
# event handling
s.listen()
s.onkey(MoveUp,"Up")
s.onkey(MoveDown,"Down")
s.onkey(MoveRight,"Right")
s.onkey(MoveLeft,"Left")
s.onkey(MoveStop,"space")
        
        
    
while True:
    s.update()
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)
    
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("white")
        body.fillcolor("green")
        bodies.append(body)
        
        score += 1
        delay -= 0.001
        if score > highscore:
            highscore = score
            
            
        
            
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    Move()
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            go = turtle.Turtle()
            go.color("red")
            go.goto(0 , 0)
            go.write("Game Over")
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("score:{} highestscore:{}".format(score,highscore))
            
            
            
            
               
            
            
    # if len(bodies) > 0:
    #     x = head.xcor()
    #     y = head.ycor()
    #     bodies[0].goto[x,y]
        
       
        
    
    time.sleep(delay)
s.mainloop()

