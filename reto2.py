from random import randint
import os
INITIAL_pikachu_live=90
INITIAL_squirtle_live=90

squirtle_live= INITIAL_squirtle_live
pikachu_live= INITIAL_pikachu_live



while squirtle_live >0 and pikachu_live>0:
    #now the combat starts
    #Pika turn
    pika_attack= randint(1,2)

    if pika_attack==1 :

        print("Pikachu attacks with voltio ball")
        squirtle_live-=10
    else:

        print("Pikachu attacks with thunder")
        squirtle_live-=11

    #print("the live of pika is: {} ,the live of squirtle is: {}".format(pikachu_live,squirtle_live) )

    pika_bar = int( pikachu_live*10/INITIAL_pikachu_live)
    print("Pikachu:  [{}{}][{}/{}]".format("*" *  pika_bar, " " * (10-pika_bar) ,pikachu_live,INITIAL_pikachu_live))
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
        print("Pikachu:  [{}{}][{}/{}]".format("*" *  pika_bar, " " * (10-pika_bar) ,pikachu_live,INITIAL_pikachu_live))
        squirtle_bar = int( squirtle_live*10/INITIAL_squirtle_live)
        print("Squirtle:  [{}{}][{}/{}]".format("*" * squirtle_bar, " " *(10-squirtle_bar),squirtle_live,INITIAL_squirtle_live))

        input("press enter to continue...\n\n")
        os.system("clear")
if(pikachu_live>squirtle_live):
    print("squirtle pierde! pika gana")
else:
    print("squirtle gana")

