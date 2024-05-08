



# Dado un string, utiliza un bucle for para contar cuántas veces aparece la 
# letra 'a' en el string.



palabrita=input('a contar esas aes! dame tu palabra: ')
counter=0
for letra in palabrita:
    if(letra.count('a')):
        counter+=1
print(counter)

#si no fuera que hay que usar el for, con palabra.count ya salen todas las apariciones XD por eso es mejor la solución del profe, aunque no sé cuál es más costosa, igual es más simple y legible la del profe 

""" texto = "banana"
contador = 0
for caracter in texto:
    if caracter == 'a':
        contador += 1
print(f"La letra 'a' aparece {contador} veces en la palabra {texto}.")




 """