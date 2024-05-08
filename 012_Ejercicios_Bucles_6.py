

# Escribe un script que cuente desde 1 hasta un número n proporcionado por 
# el usuario, imprimiendo cada número.

def pedidoNumerico():
    try:
        return(int(input('hola! querés que imprimamos cada número del que se compone tu número? eh? no se entendió? mirá... pasame un número: ')))
    except:
        print('eso no es un número, parece XD vamos de vuelta?')
        return pedidoNumerico()
numeroMagico=pedidoNumerico()

if(numeroMagico<0):
    for n in range(0, numeroMagico-1, -1):
        print(n)
        
for n in range(0, numeroMagico+1):
    print(n)

""" 
n = int(input("Introduce un número hasta el que contar: "))
contador = 1
while contador <= n:
    print(contador)
    contador += 1 """



