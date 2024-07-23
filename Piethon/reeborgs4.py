def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()  
for i in range(3):
    move()
turn_left()
for i in range(3):
    move()
turn_right()
move()
turn_right()
while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
think(100)
turn_right()
turn_right()
move()
if wall_in_front():
    turn_right()
move()
while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
think(100)
turn_right()
turn_right()
move()
if wall_in_front():
    turn_right()
while front_is_clear():
    move()
    if wall_in_front():
        turn_left() 
