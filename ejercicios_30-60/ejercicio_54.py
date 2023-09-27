def sumatoriaDigitos(numero):
    suma_digitos = 0
    while numero != 0:
        ultimo_digito = numero % 10
        suma_digitos += ultimo_digito
        numero = numero // 10
    return suma_digitos
        
def esPar (numero):
    if numero % 2 == 0:
        return True             
    elif numero % 2 != 0:
        return False


cantidad_num_impares = 0
num_entero = int(input("Ingresa un numero entero: "))

while num_entero % 5 != 0:
    if sumatoriaDigitos(num_entero) > 1000:
        break
    if not esPar(num_entero):
        cantidad_num_impares += 1
    num_entero = int(input("Ingresa un numero entero: "))

print(f"Se ingresaron {cantidad_num_impares} numeros impares en total")
