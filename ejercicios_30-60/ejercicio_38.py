numeros = [0, 1]
for x in range(8):   
    numeros.append(numeros[-2] + max(numeros))
print(numeros)