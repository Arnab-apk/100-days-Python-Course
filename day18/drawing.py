import turtle as turtle_module
from turtle import Screen
import random

screen=Screen()

turtle_module.colormode(255)
tim=turtle_module.Turtle()
color_list=[(202,164,109),(238,248,245),(150,75,49),(150,75,49),(223,281,135),(52,93,124)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

tim.setheading(90)
tim.forward(50)
tim.setheading(180)

screen.exitonclick()