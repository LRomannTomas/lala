monto = float(input("Ingresa el monto de una venta: "))
total = 0

while monto != 0:
    if monto < 0:
        print("Monto no valido")
        monto = float(input("Ingresa el monto de una venta: "))
    elif monto > 0:
        total = total + monto
        print(f"El monto de una venta: ${monto}")    
        monto = float(input("Ingresa el monto de una venta: "))
if total > 1000:
    print(f"El monto total a pagar es: ${total - (total * 0.1)} " )
else :  
    print(f"El monto total a pagar es: ${total}")


