import readchar
import os
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_Of_MAP_OBJECTS = 11

my_position = [3,1]
map_objects =[]
tail_length=0
tail=[]

#Main loop
end_game = False
while not end_game:

    #generate random objects on the map

    while len (map_objects) < (NUM_Of_MAP_OBJECTS):
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0,MAP_HEIGHT)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    print("+" + "-" *MAP_WIDTH*3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
    
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell =None
            tail_in_cell= None
            for map_object in map_objects:
                if map_object[POS_X]==coordinate_x and map_object[POS_Y]== coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail :
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y]== coordinate_y:
                   char_to_draw = "@" 
                   tail_in_cell = tail_piece
                

            if my_position[POS_X]==coordinate_x and my_position[POS_Y]== coordinate_y:
                char_to_draw = "@"
        
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length+=1
                if tail_in_cell:
                   
                    end_game=True

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" *MAP_WIDTH*3 + "+")
    print("lenght tail {}".format(tail_length))
    #Ask user where he wants to move

    # direction = input("Where do you want to move?[WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0,my_position.copy())
        tail = tail[0:tail_length]
        my_position[POS_Y]-= 1
        my_position[POS_Y]%= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0,my_position.copy())
        my_position[POS_Y]+= 1
        my_position[POS_Y]%= MAP_HEIGHT
        tail = tail[0:tail_length]
    elif direction == "a":
        tail.insert(0,my_position.copy())
        my_position[POS_X]-= 1
        my_position[POS_X]%= MAP_WIDTH
        tail = tail[0:tail_length]
    elif direction == "d":
        tail.insert(0,my_position.copy())
        my_position[POS_X]+= 1
        my_position[POS_X]%= MAP_WIDTH
        tail = tail[0:tail_length]
    elif direction=="u":
        break

    os.system("clear")
    print("you lose")