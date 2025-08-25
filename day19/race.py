from turtle import Turtle ,Screen

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your Bet-",prompt="Which turtle will win the race enter the colour- ")
print(user_bet)
tim=Turtle(shape="turtle")
tim.penup()

tim.goto(x=-230,y=-100)
screen.exitonclick()
