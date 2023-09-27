frase = str(input("Ingrese una frase: "))
caracter = str(input("Ingrese una unica letra: "))
for x in frase:
    if x == caracter:
        frase_nueva = frase.replace(caracter , "*")
print(frase_nueva)