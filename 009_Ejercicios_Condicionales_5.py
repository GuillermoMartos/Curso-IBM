

# Escribe un programa que pida al usuario un número del 1 al 7 y muestre el día 
# de la semana correspondiente. Si el número no está en ese rango, debe 
# indicar que el número es inválido.
def numerador():
    try:
        return int(input("Ingresa un número del 1 al 7: "))
    except:
        print('vamos de nuevo... a ver si prestás atención, pibæ...')
        return numerador()

numero=numerador()       

while(numero>7 or numero<=0):
    print('del 1 al 7, estás sordæ? XD')
    numero=numerador()
    
if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
