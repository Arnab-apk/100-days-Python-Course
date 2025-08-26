from turtle import Turtle ,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your Bet-",prompt="Which turtle will win the race enter the colour- ")
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-
       10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    y=100
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>250:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won.The colour of the winning turtle is:{winning_color}")
            else:
                print(f"You lost.The colour of the winning turtle is:{winning_color}")
           
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
    
    
screen.exitonclick()
