

# Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
# Escribe un programa que pida el total de la compra y calcule el descuento 
# (si aplica) y el total a pagar.

# Solicita al usuario que ingrese el total de la compra
def aVerElTicketMaestro():
    try:
        return float(input("Ingresa el total de la compra: €"))
    except:
        print('eso no es un número para pagar con dinero! XD vamos de vuelta...')
        return aVerElTicketMaestro()
    
compra=aVerElTicketMaestro()

if(compra>1000):
    descuento=compra*0.15
    print('descuentazo! te corresponde un descuento de €', descuento, 'tu nuevo total es €', compra-descuento)
else:
    print('gracias por sus compras! vuelvas prontos! :D')