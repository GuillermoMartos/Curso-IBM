


# Utiliza un bucle for para generar e imprimir la lista de los cuadrados 
# de los primeros 10 números enteros (1 al 10).
listaCuadraticaLoca=[]
for poxipol in range(1,11):
    listaCuadraticaLoca.append(poxipol*poxipol)
    print(listaCuadraticaLoca)


# esta solución del profe es mejor porque si fuera al cubo o más empezaría a repetir mucho XD el ** reemplaza al ^
cuadrados = []
for numero in range(1, 11):
    cuadrados.append(numero ** 2)
print("Cuadrados de los números del 1 al 10:", cuadrados)

























