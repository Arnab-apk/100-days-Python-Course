import random
word=["aardvark","baboon","camel"]
rand_word=random.choice(word)
print(rand_word)
len=len(rand_word)
placeholder=""
for position in range(0,len):
    placeholder+="_"
print(placeholder)
char=input("Guess a letter: ").lower()

for letter in rand_word:
    if(char==letter):
        print(char)
    else:
        print("wrong")
