

# Una tienda ofrece descuentos basados en el total de compra. 
# Si la compra es mayor a €100, el descuento es del 10%. Si es mayor a €500, 
# el descuento es del 20%. Crea un programa que calcule el total a pagar 
# después del descuento.

def calculaTickets():
    try:
        return float(input("Introduce el total de la compra: €"))
    except:
        print('vamos... eso no es un formato de moneda, wey...')
        return calculaTickets()

compra =  calculaTickets()
if compra > 500:
    descuento= compra*0.2
    print(f"El total después del descuento es: €{descuento}, o sea vamos a pagar: €{compra- descuento}")
else:
    if compra > 100:
        descuento= compra*0.1
        print(f"El total después del descuento es: €{descuento}, o sea vamos a pagar: €{compra- descuento}")
    else:
        print(f"No hay descuento. El total es: €{compra}")
