#frase = (input("Ingrese una frase: "))
#vocales = 0
#for x in frase:
 #   if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
  #      vocales = vocales + 1
#
#print(f"Hay {vocales} vocales en tu frase")

frase = (input("Ingrese una frase: "))
vocales = "aeiou"
cant_vocales = 0

for x in frase:
    if x in vocales:
        cant_vocales = cant_vocales + 1

print(f"Hay {cant_vocales} vocales en tu frase")
