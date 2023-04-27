#Escapar del barco pirata como prisionero

#1 Te encuentras atrapado en la celda y se le caen las llaves al guardia
    #coges las llaves?
        #SI -
        # A abrir la puerta directamente y  escapar o B esperar a q se haga de noche

            #A: El guardia te pilla y se acaba el juego

            #B: Ya es de noche sales y estan todos los guardias durmiendo
                #A Salir silencioso
                    #te encuentras una moneda de oro la coges?
                        #Si
                        #No
                        
                        #Una vez estas fuera el capitan del barco te pilla 
                            #Te pregunta si puedes comprar tu libertar en el caso de haber cogido la moneda podras escapar
                            #Si no la has cogido te volveran a meter a la celda

                #B Salir corriendo haciendo ruido
                    #consigues llegar a un bote y huir
        #No coges llaves 
        #- Te quedas en la celda esperando otra oportunidad al dia siguiente


print ("Escapa del barco Pirata\n"
       "------------------------"
        "\n"
        "\n"
       "Unos piratas te han hecho prisionero en su barco tras atacar al tuyo\n" 
        "debes encontrar la manera de huir\n")

print ("Estas dentro de la prision en la bodega...\n"
        "Un guardia de seguridad borracho por el ron.\n"
        "Pasa por delante de tu celda y se le caen las llaves.\n")

#objetos que se usan
llaves=False
moneda =False

opcion = input("[OPCION (A)- Coges las llaves]\n"
               "[OPCION (B) - No las coges y esperas otra oportunidad]:\n")

if opcion == "A":
       llaves=True
       print ("Ahora ya estas mas cerca de escapar\n")
       opcion = input("[OPCION (A)- Esperas a la noche ]\n"
               "[OPCION (B) - Abres la puerta y sales corriendo directamente]:\n")
       if opcion == "A":
            print ("Ahora ya estas mas cerca de escapar\n")
            print ("Ya es de noche y parece que todo el mundo esta durmiendo\n")
            print ("Decides salir \n")
            opcion = input("[OPCION (A)- Salir rapido sin importar hacer ruido ]\n"
               "[OPCION (B) - salir silenciosamente]:\n")
            if opcion == "A":
                   print ("Has hecho mucho ruido y se han despertado vuelves a la celda\n")
            else:
                print ("Al ir de forma silenciosa te encuentras con una bolsa de monedas\n")
                opcion = input("[OPCION (A)- la coges ]\n"
               "[OPCION (B) - No y sigues hacia delante]:\n")
                if opcion == "A": 
                      moneda=True
                print ("Ya estas fuera pero justo cuando vas a subirte al bote te encuentras con el capitan\n")
                print ("Te dice que puedes comprar tu libertad pero has cogido las monedas?....\n")
                if moneda == True: 
                      print ("Si las cogiste y ahora eres libre!\n")
                else:
                      print ("Vaya... no las cogiste y volviste a caer presoo\n")

       else:
              print("Vaya te han pillado y te han metido en la celda de nuevo:(\n")


else:
        print("Vaya perdiste tu oportunidad de escapar tendras q esperar a otra:(\n")