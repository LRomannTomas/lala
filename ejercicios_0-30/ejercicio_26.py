edad = int(input("Decime tu edad: "))
articulos_comprados = int(input("Cuantos articulos compraste?: "))
print(f"Sos mayor de 18 años y compraste mas de un articulo: {(edad > 18) and articulos_comprados > 1}")