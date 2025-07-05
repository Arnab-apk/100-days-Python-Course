from art import logo
from data import famous_people
import random
#ascii art to show

print(logo)
#generate a random account from the game
account_a=random.choice(famous_people)
account_b=random.choice(famous_people)
if account_a == account_b:
    account_b=random.choice(famous_people)

#format the account data into printable format
#ask the user for a guess
#check if user is correct
##get follower of account
###use a if statement if teh user is correct

#give the feeback on their guess
#score keeping
#make the game repeatable
#making the accounts at pos b be the next account at position a


