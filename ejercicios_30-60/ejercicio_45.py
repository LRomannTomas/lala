pregunta = input("¿Analizar calificaciones? 'S' para 'SI': ")
cantidad_alumnos = 0
cantidad_aprobados = 0
promedio_aprobados = 0
while pregunta == "S":
    calificacion = float(input("Clasificacion de un alumno: "))
    cantidad_alumnos = cantidad_alumnos + 1
    if calificacion > 4: 
        cantidad_aprobados = cantidad_aprobados + 1
        promedio_aprobados = promedio_aprobados + calificacion
    pregunta = input("Desea continuar? ")


print(f"Porcentaje de alumnos aprobados: {cantidad_aprobados * 100 / cantidad_alumnos}%")
print(f"Promedio de los aprobados: {promedio_aprobados / cantidad_aprobados}")





        