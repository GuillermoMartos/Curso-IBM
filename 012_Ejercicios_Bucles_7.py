


# Crea un programa que sume números introducidos por el usuario hasta que el 
# usuario introduzca 0. Al final, el programa debe mostrar la suma total.
listaLoka=[]
def acumulador():
    try:
        nuevoNum=int(input('ingrese num para ir sumando, o 0 para salir: '))
        if(nuevoNum!= 0):
            listaLoka.append(nuevoNum)
            return acumulador()
        else: return listaLoka
    except:
        print('eso no era un numerou! vamos otra vuelta!')
        return acumulador()

acumulador()
print(sum(listaLoka), f'es el total de tu lista {listaLoka}')


""" suma = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Introduce otro número (0 para terminar): "))
print("La suma total es:", suma)


 """


