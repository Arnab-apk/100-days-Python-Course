class User:
    # this function gets called how many times a new object (user) is created
        def __init__(self,user_id,username):
            # print("new user being created!")
            self.id=user_id
            self.name=username
            self.followers=0
            self.following=0
        #methods always contain a self parameter as its first parameter as it knows the object that it calls:
        def follow(self,user):
            user.followers+=1
            user.following+=1
            
               

user_1=User("001","arnab")
# print(user_1.name)
# print(user_1.id)
# print(user_1.followers)

user_2=User("002","asmi")
# print(user_2.name)
# print(user_2.id)
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



