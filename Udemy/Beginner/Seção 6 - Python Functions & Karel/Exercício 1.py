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

for step in range(6):
    turn_finaly()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
