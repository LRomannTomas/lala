#numero=int(input("Número (-1 para terminar el programa):"))
#while numero!=-1:
#    if numero%3 == 0:
#        multiplosDe3=multiplosDe3+1
#    digitosPares=0
#    digitosImpares=0
#    while numero!=0:
#        ultimodigito=numero%10
#        if ultimodigito%2==0:
#           digitosPares=digitosPares+1
#        else:
#            digitosImpares=digitosImpares+1
#        numero=numero//10
#    print("Dígitos pares:", digitosPares)
#    print("Dígitos impares:", digitosImpares)
#    numero=int(input("Número (-1 para terminar el programa):"))
#print("Se ingresaron", multiplosDe3, "múltiplos de 3.")


pan = 3.49
descuento_60 = (60 * 3.49) / 100
cant_pan_vendido = int(input("Cuantos panes se vendieron?: "))
print(f"El pan, habitualmente cuesta: ${pan}")
print(f"El descuento por cada pan es: ${ pan - descuento_60}")
print(f"el coste final total es: ${descuento_60 * cant_pan_vendido}")


