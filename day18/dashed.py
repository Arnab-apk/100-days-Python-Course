#draw a dashed line
from turtle import Turtle,Screen
arnab=Turtle()
screen=Screen()
#
for _ in range(20):
    arnab.forward(5)
    arnab.up()
    arnab.forward(5)
    arnab.down()
    
screen.exitonclick()