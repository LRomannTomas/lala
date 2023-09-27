numero = float(input("Decime un numero positivo:"))
numeros = []

if numero > 0 :
    numeros.append(numero)

while numero > 0 :
    numero = float(input("Decime un numero positivo: "))
    numeros.append(numero)

numero_mayor = int(max(numeros))
print(f"el numero mas grande ingresado es {numero_mayor}")
