# --------------------------------
# pseudo functions to make the errors go away
# --------------------------------

def turn_left():
    print("turn left")
    
def move():
    print("move")

def wall_in_front():
    wall_front = True #or false
    return wall_front

def right_is_clear():
    right_clear = True # or false
    return right_clear

def at_goal():
    goal = True
    return goal

# --------------------------------
# actual code. This code only works on the reeborgs website, and the above code is just to remove the errors out, because these functions are built in into the reeborg website. Head there to test the below code.
# --------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_wall():
    while not wall_in_front():
        move()
    turn_left()

def reach_goal():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif wall_in_front():
            turn_left()
        else:
            move()
   
find_wall()
reach_goal()
# =============
# reeborg