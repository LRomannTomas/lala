cadena = input("Titulo del libro: ")
numeros = "0123456789"
cant_numeros = 0
cant_lineas = 0

while cadena != "/":
    for num in cadena:
        if num in numeros:
            cant_numeros += 1
    cadena = input("Titulo del libro: ")

    if cadena == "/":
        print(f"Aparecen {cant_numeros} digitos en la línea")
        cant_lineas += 1
        cant_numeros = 0
        cadena = input("Titulo del libro: ")

    if cadena == "*":
        print(f"Se leyeron {cant_lineas} lineas completas")
        break

