def esPalindroma(texto):
    texto_inversa = ""
    for chars in texto:
        texto_inversa = chars + texto_inversa
    if texto_inversa == texto:
        return True
    elif texto_inversa != texto:
        return False

frase = input("Ingresa una frase: ")
frase = frase.lower()
cantidad_palindromas = 0
if esPalindroma(frase):
    cantidad_palindromas += 1
while frase != "fin":
    frase = input("Ingresa una frase: ")
    frase = frase.lower()
    if esPalindroma(frase):
        cantidad_palindromas += 1

print(f"cantidad de palindromas: {cantidad_palindromas}")
