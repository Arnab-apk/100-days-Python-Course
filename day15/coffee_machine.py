from art import coffee
#coffee machine project
#ascii art to show
print(coffee)
#printing report
#check if resources are sufficient
#check if transaction is successful
#processing coins
#make coffee
water=100
milk=50
coffee=76
money=0.0
#indivijual costs
cost_exspresso=1.5
cost_latte=2.5 
cost_cappuccino=3.0
type=input("What would you like? (espresso/latte/cappuccino): ")
should_continue=True
while should_continue:
    if type=="report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    elif type=="espresso":
        if water>=50 and coffee>=18:
            print("Please insert coins.")
            quarters=int(input("How many quarters? ")) * 0.25
            dimes=int(input("How many dimes? ")) * 0.10
            nickels=int(input("How many nickels? ")) * 0.05
            pennies=int(input("How many pennies? ")) * 0.01
            total=quarters + dimes + nickels + pennies
            if total>=cost_exspresso:
                change=total-cost_exspresso
                money+=cost_exspresso
                water-=50
                coffee-=18
                print(f"Here is ${change:.2f} in change.")
                print("Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif type=="latte":
        if water>=200 and milk>=150 and coffee>=24:
            print("Please insert coins.")
            quarters=int(input("How many quarters? ")) * 0.25
            dimes=int(input("How many dimes? ")) * 0.10
            nickels=int(input("How many nickels? ")) * 0.05
            pennies=int(input("How many pennies? ")) * 0.01
            total=quarters + dimes + nickels + pennies
            if total>=cost_latte:
                change=total-cost_latte
                money+=cost_latte
                water-=200
                milk-=150
                coffee-=24
                print(f"Here is ${change:.2f} in change.")
                print("Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif type=="cappuccino":
        if water>=250 and milk>=100 and coffee>=24:
            print("Please insert coins.")
            quarters=int(input("How many quarters? ")) * 0.25
            dimes=int(input("How many dimes? ")) * 0.10
            nickels=int(input("How many nickels? ")) * 0.05
            pennies=int(input("How many pennies? ")) * 0.01
            total=quarters + dimes + nickels + pennies
            if total>=cost_cappuccino:
                change=total-cost_cappuccino
                money+=cost_cappuccino
                water-=250
                milk-=100
                coffee-=24
                print(f"Here is ${change:.2f} in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    else:
        print("Invalid input. Please try again.")
    type=input("What would you like? (espresso/latte/cappuccino/report): ")
    if type == "off":
        should_continue = False
        print("Turning off the coffee machine. Goodbye!")   
