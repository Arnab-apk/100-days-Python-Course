# global modification
enemies=1

def increase_enemies():
    #global scope modificaton in local scope
    global enemies
    enemies+=1
    print(enemies)

increase_enemies()
print(f"enemies outside function {enemies}")




