def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()  
def harvest_one_row():
    while object_here():
        take()
        move()
def right():
    turn_right()
    move()
    turn_right()
    move()
def left():
    turn_left()
    move()
    turn_left()
    move()
for i in range(2):
    move()
turn_left()
move()
move()
harvest_one_row()
right()
harvest_one_row()
left()
harvest_one_row()
right()
harvest_one_row()
left()
harvest_one_row()
right()
harvest_one_row()
left()
