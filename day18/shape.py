from turtle import Turtle,Screen
from random import Random
random=Random()
turtle=Turtle()
screen=Screen()

turtle.pensize(3)

def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)

for i in range(3,11):
    turtle.color(random_color())
    for j in range(i):
        turtle.forward(100)
        turtle.right(360.0/i)

screen.exitonclick()

