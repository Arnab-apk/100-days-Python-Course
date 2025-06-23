print("welcome to th e roller coaster!")
height=int(input("What is your height? "))
age=int(input("What is your age? "))
ticket=0
if height>=120:
    print("Hurray you can ride the roller coaster!")
    if age<12:
        ticket=5
        print(f"pay{ticket}$")
    elif 12<age<18:
        ticket=7
       
    else:
        ticket=12
      
    photo=input("Do you want to have a photo take? Type y for Yes and n for No- ")
    if(photo=='y'):
        ticket+=3
        print(f"Pay {ticket}$ including the photo")
    else:
        print(f"Pay {ticket}$ excluding the photo")
        
else:
    print("Sorry cant ride the roller coaster!") 