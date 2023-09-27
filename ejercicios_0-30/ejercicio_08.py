
telefono = input("Ingrese el numero de telefono con el siguiente formato prefijo-numero-extension: ")


posicion_guion1 = telefono.find("-")


posicion_guion2 = telefono.find("-", posicion_guion1 + 1)


numero_telefono = telefono[posicion_guion1 + 1 : posicion_guion2]

print("Número de teléfono sin prefijo ni extensión:", numero_telefono)