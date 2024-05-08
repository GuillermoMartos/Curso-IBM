

# Escribe un script que solicite una calificación al usuario (0 - 100). 
# Si la calificación es mayor o igual a 90, imprime "Excelente", si es mayor 
# o igual a 70 y menor que 90, imprime "Bueno", si es mayor o igual a 50 y 
# menor que 70, imprime "Suficiente", y si es menor que 50, imprime "Insuficiente".

def inputDeNota():
    try:
        notita=int(input('dame tu notita del 0 al 100: '))
        if(notita>100 or notita < 0):
            print('no se puede pasarse de 100 o menos que cero, che!')
            return inputDeNota()
        if(notita >= 90):
            return print('Excelente')
        if(notita >= 70):
            return print('Bueno')
        if(notita >= 50):
            return print('Suficiente')
        else:
            print('Insuficiente')
    except:
        print('creo que tu notita no es un número... vamos otra vez? ')
        inputDeNota()

inputDeNota()

