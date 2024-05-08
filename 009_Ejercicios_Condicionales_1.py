

# Escribe un programa que pregunte al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

def inputEdad(edad):
    try:
        return int(edad)
    except:
        print('tu edad debe ser un número, che!')
        return False
pedirEdad=input('decime tu edad que te digo otra cosa:')


edad= inputEdad(pedirEdad)
while(edad==False):
      pedirEdad2=input('dale, intentemos de nuevo tu edad... ')
      edad=inputEdad(pedirEdad2)

if(edad>=18):
    print("sos mayor de edad al tener ya tus", edad, "añitos! XD")
else:
    print("no sos mayor de edad... pero te faltan tan solo", 18-edad,"añitos para serlo! Ánimo! XD")