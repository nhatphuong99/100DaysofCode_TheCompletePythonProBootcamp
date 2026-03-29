#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function

'''
# Hurdles race
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    jump()

# Hurdles 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
# Hurdles 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
# Maze Easy
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Maze Hard
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
  
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''