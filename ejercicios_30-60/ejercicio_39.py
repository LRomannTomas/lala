numero = int(input("Decime un numero entero positivo: ")) 
lista = [1]
for x in range(1,numero + 1):
    cuenta = x * lista[-1]
    lista.append(cuenta)

factorial = max(lista)
int(factorial)
print(f"El factorial de {numero} es {factorial}")
