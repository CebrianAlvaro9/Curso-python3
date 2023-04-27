lista_compra=[]

input_usuario= None

print("Programa lista de la compra \n")

while True:
    input_usuario=input("Que desea comprar [Q] para salir: ")
    if input_usuario=="Q":
        break
    elif input_usuario in lista_compra:
        print("{} ya esta en la lista de la compra".format(input_usuario))
    else:
        if input("Seguro que quieres  anadir {} S/N:  ".format(input_usuario))=="S" :
            lista_compra.append(input_usuario)
print("La lista de la compra es: ")
print(lista_compra)