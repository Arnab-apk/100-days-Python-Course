from turtle import Screen,Turtle
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
starting_pos=[(0,0),(-20,0),(-40,0)]

segments=[]



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

    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    
        
  
        
screen.exitonclick()