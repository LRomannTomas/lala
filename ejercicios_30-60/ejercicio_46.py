caracter = input("Escribi un solo caracter: ")
string_completo = ""
cantidad_letras_a = 0
while len(caracter) == 1 or len(caracter) != 1 :

    if len(caracter) == 1:
         string_completo = string_completo + caracter
         caracter = input("Escribi un solo caracter: ")

    elif len(caracter) != 1:
         print(f"El string completo es: {string_completo}")
         break

for a in string_completo:
    if a == "a":
        cantidad_letras_a = cantidad_letras_a + 1
    
if cantidad_letras_a <= 0:
    print(f"Porcentaje de letras 'a': {cantidad_letras_a}%")
elif cantidad_letras_a > 0:
    print(f"Porcentaje de letras 'a': {cantidad_letras_a * 100 / len(string_completo)}%")


