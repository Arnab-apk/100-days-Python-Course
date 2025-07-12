import turtle as t 
from turtle import Screen

screen=Screen()
import random

def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)

tim=t.Turtle()
rand=random.Random()
tim.pensize(3)
directions=[0,90,180,270]
for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

screen.exitonclick()

#turtle gone aimless