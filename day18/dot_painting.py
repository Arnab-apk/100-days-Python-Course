import turtle as t
from turtle import screen as s
import random

turtle=t.Turtle()
screen=s.Screen()
turtle.colormode(255)
def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)

for _ in range(10):
    t.dot(20,random_color())
    t.forward(50)
    
screen.exitonclick()


