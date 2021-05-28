#realizado por Yovany Ferney Toro Botero
producto = (input("ingrese el producto: "))
cantidad = int(input("ingrese la cantidad: "))
Valunitario = int(input("ingrese el valor unitario: "))
ciudadVent = (input("ingrese la ciudad de venta: "))

total = 0 
total = cantidad*Valunitario

if ciudadVent=="medellin" or ciudadVent=="cali":
    total= total*0.95
    print("el valor con el descuento es de: ", total)
else:
    print("No se aplica el descuento")
    print("su total a pagar es: ", total)