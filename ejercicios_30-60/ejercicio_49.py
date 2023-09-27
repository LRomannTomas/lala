cadena_chars = input("Escribi una cadena de caracteres: ")
letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
cantidad_letras = 0
cantidad_numeros = 0
cantidad_simbolos = 0
multiplos_de_4 = 0

for x in cadena_chars:
    for chars in letras:
        if chars == x:
            cantidad_letras += 1
    for num in numeros:
        if num == x:
            cantidad_numeros += 1
            if int(x) % 4 == 0:
                multiplos_de_4 += 1
    if x not in letras and x not in numeros:
        cantidad_simbolos += 1

    

print(f"Hay {cantidad_letras} letras")
print(f"Hay {cantidad_numeros} numeros")
print(f"Hay {cantidad_simbolos} simbolos")
print(f"Hay {multiplos_de_4} multiplos de 4")

        
        

