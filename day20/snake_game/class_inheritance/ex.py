class animal():
    def __init__(self):
        self.eyes=2
    def breath(self):
        print("inhale exhale")

class fish(animal):
    def __init__(self):
        super().__init__()
    
    def breath(self):
        super().breath()
        print("dooooiing itt underr watterr!")
    
    def swim(self):
        print("Movving underr waterrr!") 
           
nemo=fish()
nemo.breath()
print(nemo.eyes)

#we can inherit the methods from other class using the super function intoa nother class and bring added functionality into it

