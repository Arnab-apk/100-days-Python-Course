import art
print(art.art)
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}
#accesing the function using key 
# print(operations["*"](4,5))
def calculator():
    should_accumulate=True
    num1=float(input("What is the first number?: "))
    while(should_accumulate):
        
        for operation in operations:
            print(operation)

        operation_sym=input("Pick an operation: ")
        num2=float(input("What is the next numbers?: "))
        answer=operations[operation_sym](num1,num2)
        print(f"{num1} {operation_sym} {num2} = {operations[operation_sym](num1,num2)}")
        choice=input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation: ")
        if(choice=="y"):
            num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            #tail recursion
            calculator()
            
calculator()




