import random
word=["aardvark","baboon","camel"]
rand_word=word[(random.randint(0,2))]
len=len(rand_word)
char=input("Guess a letter: ")

for letter in rand_word:
    if(char==letter):
        print("true")
    else:
        print("false")


