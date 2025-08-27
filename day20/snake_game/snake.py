
from turtle import Turtle
Starting_pos=[(0,0),(-20,0),(-40,0)]
class Snake:
    
    def _init_(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for position in Starting_pos:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)    
        