from turtle import Turtle,Screen
from random import Random
random=Random()
turtle=Turtle()
screen=Screen()
turtle.speed("fastest")
turtle.width(1)
def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)
def draw_spi(size):
    for _ in range(int(360/size)):
        turtle.color(random_color())
        turtle.circle(100)
        current_heading=turtle.heading()
        turtle.setheading(current_heading+size)
        turtle.circle(100)
        
draw_spi(5)
screen.exitonclick()

