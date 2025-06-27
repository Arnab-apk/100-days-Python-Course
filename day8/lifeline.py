print("Welcome to Life in Weeks:")
def life_in_weeks(age):
    rem=90-age
    weeks=rem*52
    print(f"You have {weeks} weeks left" )
age=int(input("Enter your curent age: "))
life_in_weeks(age)