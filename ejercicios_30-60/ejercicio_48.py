numero = int(input("Ingresa un numero entero positivo(-1 para finalizar el programa): "))
multiplos_de_3 = 0
digitos_pares = 0
digitos_impares = 0


while numero != -1 :
    if numero % 3 == 0:
        multiplos_de_3 = multiplos_de_3 + 1

    while numero != 0:
        ultimo_digito = numero % 10
        if ultimo_digito % 2 == 0:
            digitos_pares = digitos_pares + 1
            
        else:
            digitos_impares = digitos_impares + 1

        numero = numero // 10
   
    print(f"Digitos pares: {digitos_pares}")
    print(f"Digitos impares: {digitos_impares}")
    numero = int(input("Ingresa un numero(-1 para finalizar el programa): "))


