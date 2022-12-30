#Modigy global scope inside the function

enemies = 1  

def increase_enemies():
    global enemies 
    enemies += 1
    print(f"enemies inseide function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")