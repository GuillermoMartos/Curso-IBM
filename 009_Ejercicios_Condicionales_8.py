

# Escribe un programa que sugiera qué ponerse basado en la temperatura actual 
# (en grados Celsius) que el usuario introduce. Considera:

# Menos de 10°C: Abrigo y bufanda.
# De 10°C a 20°C: Suéter ligero.
# Más de 20°C: Camiseta.

def temperometro():
    try:
        return float(input('temperatura actual en la ciudad en grados Celsius es: '))
    except:
        print('eso no es un numero... probemos de nuevo, dale?')
        return temperometro()
    

temperatura = temperometro()
if temperatura < 10:
    print("Deberías usar abrigo y bufanda.")
else:
    if temperatura <= 20:
        print("Un suéter ligero sería adecuado.")
    else:
        print("Es un buen día para llevar camiseta.")
