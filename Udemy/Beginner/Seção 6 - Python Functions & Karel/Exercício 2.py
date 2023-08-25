def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_finaly():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    turn_finaly()
    
# or 
# while not at_goal():
# turn_finaly()