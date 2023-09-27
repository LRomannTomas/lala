numero = 0
suma_pares = 0
suma_impares = 0

def esPar (numero):
    if numero % 2 == 0:
        return True             # ---> no es neceserio aclarar que se retorne un booleano. Con que esa condicion se cumpla retorna True , sino retorna False.
    elif numero % 2 != 0:
        return False

for num in range(10):
    numero = int(input("Decime un numero: "))
    if esPar(numero) == True:
        suma_pares += numero
    elif esPar(numero) == False:
        suma_impares += numero
    

print(f"Suma de los pares: {suma_pares}")
print(f"Suma de los impares: {suma_impares}")

#Funciona pero se puede mejorar.