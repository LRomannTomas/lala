letra = (input("Escribi una letra en Mayuscula: "))

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"{letra} es vocal")

elif len(letra) != 1:
    print("No se puede procesar el dato")
    