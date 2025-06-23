print("Welcome to the tip Calculator!")
bill=float(input("What was the total bill? $"))
tp=int(input("How much tip would you like to pay? "))
n=int(input("How many people to split the bill? "))
tip=(bill*tp)/100
final=(bill+tip)/n
print(f"each person should pay: ${round(final,2)}")