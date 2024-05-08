

# Escribe un programa que pida la edad del usuario y clasifique a las personas en diferentes categorías (niño, adolescente, adulto, adulto mayor). Supón los siguientes rangos de edad:

# Niño: Menos de 13 años.
# Adolescente: De 13 a 19 años.
# Adulto: De 20 a 64 años.
# Adulto mayor: 65 años o más.

def edadometro():
    try:
        return int(input("Introduce tu edad: "))
    except:
        print('esa no es una edad edable! XD edadifiquemos de nuevo jajajaj')
        return edadometro()

edad = edadometro()
if edad <= 0:
    print('no eres ni un feto XD')
if edad < 13:
    print("Eres un niño.")
else:
    if edad < 20:
        print("Eres un adolescente.")
    else:
        if edad < 65:
            print("Eres un adulto.")
        else:
            print("Eres un adulto mayor.")
