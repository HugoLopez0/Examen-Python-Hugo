
cantidades = input("Ingrese las cantidades de velas: ").split(sep=",")

mayor = 0
contador = 0

for i in range(0, len(cantidades)):
    if mayor < int(cantidades[i]):
        mayor = int(cantidades[i])

for j in range(0, len(cantidades)):
    if mayor == int(cantidades[j]):
        contador = contador + 1

print(contador)



