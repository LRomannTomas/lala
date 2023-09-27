sumatoria_negativos = 0
promedio_positivos = 0
cantidad_positivos = []
for x in range(6):
    numeros = int(input("Ingresa un numero: "))
    if numeros < 0:
        sumatoria_negativos = sumatoria_negativos + numeros
    elif numeros > 0:
        promedio_positivos = (promedio_positivos + numeros) 
        cantidad_positivos.append(numeros)

print(f"la sumatoria de los numeros negativos es: {sumatoria_negativos}")


if len(cantidad_positivos) != 0:
    print(f"el promedio de los numeros positivos es: {promedio_positivos / len(cantidad_positivos)}")

else: 
    print("No se puede obtener un promedio de los numeros positivos ya que no es posible divir por 0")



