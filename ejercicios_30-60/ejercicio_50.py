numero = input("Ingresa un numero (Se finaliza si es multiplo de 10 o menor a 0): ")
string1 = ""
string2 = ""
while numero[-1] != "0" and numero[0] != ("-"):
    if len(numero) % 3 == 0:
        string1 += numero + "-"

    for x in numero:
        if x == "0":
            string2 += numero + "-"
            break
    numero = input("Ingresa un numero (Se finaliza si es multiplo de 10 o menor a 0): ")
    
print(f"Números cuya cantidad de dígitos es múltiplo de 3: {string1}")
print(f"Números que contienen 0: {string2}")

