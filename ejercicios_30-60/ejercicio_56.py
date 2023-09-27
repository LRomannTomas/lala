def iniciaCon9(num):
    for numeros in num:
        if (numeros[0]) == "9":
            return True
        elif (numeros[0]) != "9":
            return False
    int(num)

def cantidadDivisores(numero):
    cantidad_divisores = 0
    for divisores in range (1, numero +1):
        if numero % divisores == 0:
            cantidad_divisores += 1
    return cantidad_divisores


numero = input("Ingresa un numero entero: ")
numeros_con_2_divisores = 0
while iniciaCon9(numero) == False:
    numero = int(numero)
    if cantidadDivisores(numero) == 2:
        numeros_con_2_divisores += 1
    numero = (input("Ingresa un numero entero: "))

print(f"Tienen solo 2 divisores: {numeros_con_2_divisores} números")