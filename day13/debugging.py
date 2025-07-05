# debugging 1
# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("You got it")

# my_function()

# #debugging 2
# from random import randint
# dice_images=["🎲","🎲","🎲","🎲","🎲","🎲"]
# dice_num=randint(0,5)
# print(dice_images[dice_num])

# #dubugging 2
# year =int(input("What is your yaer of birth?: "))
# if year >1980 and year <1994:
#     print("You are a millennial")
# elif year >=1994:
#     print("You are a gen Z") 

# #debugging 4
# try:
#     age=int (input("How old are you? : "))
# except ValueError:
#     print("Enter your age in numbers pls typre again!")
#     age=int (input("How old are you? : "))

# if age>18:
#     print(f"You can drive at age {age}")

#debugging 5

# words_per_page=0

pages=int (input("Number of pages : "))
words_per_page=int (input("Enter the number of words per page "))
total_words=pages*words_per_page
print(total_words)

