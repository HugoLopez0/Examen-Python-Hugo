
numeros = str(input("Ingrese 2 números: ")).split(sep=",")
resultado = 0

for n in range(0, int(numeros[1])):
    resultado = resultado + int(numeros[0])

print(resultado)

