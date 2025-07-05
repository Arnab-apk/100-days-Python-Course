#debugging 1
def my_function():
    for i in range(1,21):
        if i==20:
            print("You got it")

my_function()

#debugging 2
from random import randint
dice_images=["🎲","🎲","🎲","🎲","🎲","🎲"]
dice_num=randint(0,5)
print(dice_images[dice_num])

#dubugging 2
year =int(input("What is your yaer of birth?: "))
if year >1980 and year <1994:
    print("You are a millennial")
elif year >=1994:
    print("You are a gen Z") 



