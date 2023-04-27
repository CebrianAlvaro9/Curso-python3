import os
from time import sleep
from random import randrange


def main():
    n_hours = randrange(1,4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours *60*60)
    sleep()
    desktop_path = "/home/"+os.getlogin()+"/Desktop/"

    with  open(desktop_path +"PARATI.txt", "w") as a:
        a.write("I am a hacker")
    

if __name__ == "__main__":
    main()