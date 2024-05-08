

# Solicita dos números al usuario y determina cuál de los dos es mayor o si son iguales.

def mePidoLosEnes():
    print('comparemos dos números...')
    n1=input('te pido el primer número: ')
    n2=input('te pido el segundo número: ')
    try:
        n1EsMayor = int(n1) > int(n2)
        if(n1EsMayor):
            return print ('tu primer numero es mayor jajajá!')
        else:
            return print ('tu segundo numero es mayor jujujú!')
    except:
        print('alguno no era un número, no? vamos de nuevo!... ')
        return False


result = mePidoLosEnes()
while(result == False):
    result=mePidoLosEnes()
