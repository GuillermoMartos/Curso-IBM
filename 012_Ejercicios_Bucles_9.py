




# Escribe un script que solicite al usuario su edad y asegúrate de que el 
# número proporcionado esté entre 1 y 100. Si el número está fuera de ese rango, 
# pídele que lo introduzca nuevamente.

def edadRazonable ():
    try:
        edad= int(input('metele,  a ver tu edad...'))
        if (edad > 100 or edad <= 0):
            print('no te lo creo... probemos de nuevo ://')
            return edadRazonable()
        return edad
    except:
        print('asi no!')
        return edadRazonable()

edad = edadRazonable()
print(f'mirá vos, tenés {edad} años')

""" edad = int(input("Introduce tu edad (entre 1 y 100): "))
while edad < 1 or edad > 100:
    print("Error: la edad debe estar entre 1 y 100.")
    edad = int(input("Introduce tu edad nuevamente: "))
print("Edad válida introducida:", edad)
 """


