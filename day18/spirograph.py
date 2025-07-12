from turtle import Turtle,Screen
from random import Random
random=Random()
turtle=Turtle()
screen=Screen()
turtle.speed("fastest")
turtle.width(0)
def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)
for _ in range(360):
    turtle.color(random_color())
    turtle.circle(100)
    current_heading=turtle.heading()
    turtle.setheading(current_heading+1)
    turtle.circle(100)


screen.exitonclick()

#finally made something pleasing  