numero = int(input("Numero: "))

def sumatoriaDigitos(numero):
    while numero != 100:
        suma_digitos = 0
        num = numero
        while num != 0:
            ultimo_digito = num % 10
            suma_digitos += ultimo_digito
            num = num // 10
        print(f"La sumatoria de los dígitos es: {suma_digitos}")
        numero = int(input("Numero: "))



