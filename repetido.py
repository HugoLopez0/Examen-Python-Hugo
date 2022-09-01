
palabras = input("Ingrese una cadena de texto: ").split()
palabraRepetida = ""
mayor = 0

for i in range(0, len(palabras)):
    contador = 0
    for j in range(0, len(palabras)):
       if palabras[i].lower() == palabras[j].lower():
           contador = contador + 1

    if(mayor < contador):
        mayor = contador
        palabraRepetida = palabras[i]


print(f"{palabraRepetida},{mayor}")


