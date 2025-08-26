from turtle import Screen,Turtle
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
starting_pos=[(0,0),(-20,0),(-40,0)]

segments=[]

for position in starting_pos:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# segment1=Turtle(shape="square")
# segment1.color("white")

# segment2=Turtle(shape="square")
# segment2.color("white")
# segment2.goto(-20,0)

# segment3=Turtle(shape="square")
# segment3.color("white")
# segment3.goto(-40,0)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(start=2,stop=0,step=-1):
        segments[seg_num-1]
        segments[seg_num].goto()
        
  
        
screen.exitonclick()