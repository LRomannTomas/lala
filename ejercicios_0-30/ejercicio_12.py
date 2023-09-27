precio = float(input("Precio del producto: "))
pago = float(input("Cantidad de dinero entregado por el cliente: "))

if pago > precio:
    print(f"Tu cambio es de {pago - precio} pesos")

elif pago == precio: 
    print("Se pago con lo justo!")

else: 
    print(f"faltan {precio - pago} pesos")
