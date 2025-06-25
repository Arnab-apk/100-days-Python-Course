import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
numbers=['0','1','2','3','4','5','6','7','8']
symbols=['!','#','$','%','&','(',')','*','+']



print("Welcome to the password generator: ")
nr_letters=int(input("How many letters would you like in your passowrd\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))



#easy
password=""
# #nr_letters
# for char in range(0,nr_letters):
#     password+=random.choice(letters)
# for char in range(0,nr_numbers):
#     password+=random.choice(numbers)
# for char in range(0,nr_symbols):
#     password+=random.choice(symbols)

# print(f"The password is: {password}")

#hard
password_list=[]
#nr_letters
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

#shuffling the order
random.shuffle(password_list)
print(f"The random password is: {password_list}")
             






