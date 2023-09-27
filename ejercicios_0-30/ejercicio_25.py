fecha = int(input("Decime tu fecha de nacimiento en el siguiente orden (DD/MM/AAAA): "))
print(f"{fecha // 1000000} / {(fecha % 1000000) // 10000} / {fecha % 10000}")