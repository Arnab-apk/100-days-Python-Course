from turtle import Turtle ,Screen

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your Bet-",prompt="Which turtle will win the race enter the colour- ")
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    y=100
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230,y=y_pos[turtle_index])
    
screen.exitonclick()
