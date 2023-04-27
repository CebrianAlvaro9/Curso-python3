import readchar
import os
import random 
from random import randint

pokemons =["Groudon", "Raykuaza", "Dioxis"]
def battle(pokemon):
  

    INITIAL_pikachu_live=90
    INITIAL_squirtle_live=90

    squirtle_live= INITIAL_squirtle_live
    pikachu_live= INITIAL_pikachu_live



    while squirtle_live >0 and pikachu_live>0:
        #now the combat starts
        #Pika turn
        pika_attack= randint(1,2)

        if pika_attack==1 :

            print("{} attacks with voltio ball".format(pokemon))
            squirtle_live-=10
        else:

            print("{} attacks with thunder".format(pokemon))
            squirtle_live-=11

        #print("the live of pika is: {} ,the live of squirtle is: {}".format(pikachu_live,squirtle_live) )

        pika_bar = int( pikachu_live*10/INITIAL_pikachu_live)
        print(str(pokemon)+":  [{}{}][{}/{}]".format("*" *  pika_bar, " " * (10-pika_bar) ,pikachu_live,INITIAL_pikachu_live))
        squirtle_bar = int( squirtle_live*10/INITIAL_squirtle_live)
        print("Squirtle:  [{}{}][{}/{}]".format("*" * squirtle_bar, " "*(10-squirtle_bar),squirtle_live,INITIAL_squirtle_live))


        input("press enter to continue...\n\n")
        os.system("clear")
        #squirtle turn
        if(squirtle_live>0):
            print("squirtle turn")

            squirtle_attack = None

            while squirtle_attack not in ["W","T","B"]:
                squirtle_attack = input("What is your next attack?  [W]ater Pistol, [T]ackle, [B]ubble:  ")

                if squirtle_attack=="W":
                    print("Squirtle uses Water pistol")
                    pikachu_live-=10
                elif squirtle_attack=="T":
                    print("Squirtle uses tackle")
                    pikachu_live-=12
                elif squirtle_attack=="B":
                    print("Squirtle uses Bubble")
                    pikachu_live-=9

            #print("the live of pika is: {} ,the live of squirtle is: {}".format(pikachu_live,squirtle_live) )
            pika_bar = int( pikachu_live*10/INITIAL_pikachu_live)
            print(str(pokemon)+":  [{}{}][{}/{}]".format("*" *  pika_bar, " " * (10-pika_bar) ,pikachu_live,INITIAL_pikachu_live))
            squirtle_bar = int( squirtle_live*10/INITIAL_squirtle_live)
            print("Squirtle:  [{}{}][{}/{}]".format("*" * squirtle_bar, " " *(10-squirtle_bar),squirtle_live,INITIAL_squirtle_live))

            input("press enter to continue...\n\n")
            os.system("clear")
    if(pikachu_live>squirtle_live):
        print("Has perdido fin del juego:(")
        end = True
        return end
    else:
        print("squirtle gana")




pokemon_index=0
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_Of_MAP_OBJECTS = 3

my_position = [0,1]
map_objects =[[7,1], [7,6],[18,12]]
obstacle_definition = """\
########################
           #############
           #############
#######         ########
#######       ##########
####        ############
##      ################
#   ##########      
#   ########       #####
#       #######     ####
##    ##########   #####
##    #########     ####
##                   ###
##      ######       ###  
########################\
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

#Main loop
end_game = False
while not end_game:
    os.system("clear")
    print("+" + "-" *MAP_WIDTH*3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
    
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell =None
            tail_in_cell= None
            for map_object in map_objects:
                if map_object[POS_X]==coordinate_x and map_object[POS_Y]== coordinate_y:
                    char_to_draw = "O"
                    object_in_cell = map_object
                

            if my_position[POS_X]==coordinate_x and my_position[POS_Y]== coordinate_y:
                char_to_draw = "@"
        
                if object_in_cell:
                    #aqui ira la funcion con el dominguero
                    os.system("clear")
                    
                    pokemon= pokemons[pokemon_index]

                    if(battle(pokemon)):
                        os.system("clear")
                        
                        end_game=True
                    map_objects.remove(object_in_cell)
                    pokemon_index=+1
                    os.system("clear")
                    
                
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw="#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" *MAP_WIDTH*3 + "+")
    print(map_objects)
    #Ask user where he wants to move

    # direction = input("Where do you want to move?[WASD]: ")
    direction = readchar.readchar()
    new_position =None

    if direction == "w":
        new_position=[my_position[POS_X], (my_position[POS_Y]-1)%MAP_WIDTH]
     
    elif direction == "s":
        
        new_position=[my_position[POS_X], (my_position[POS_Y]+1)%MAP_WIDTH]
      
        
    elif direction == "a":
        new_position=[(my_position[POS_X]-1)%MAP_WIDTH, my_position[POS_Y]]
       
       
    elif direction == "d":
        new_position=[(my_position[POS_X]+1)%MAP_WIDTH, my_position[POS_Y]]
      
        
    elif direction=="u":
        break
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] !="#":
            my_position=new_position
    if end_game==True:
        os.system("clear")
        print("Perdiste!")
   

    