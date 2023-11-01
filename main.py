import numpy as np
import utils

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = utils.crearMatriz(filas, columnas)

print("Matriz inicial:")
print(matriz)

solucion = utils.resolver_lights_out(matriz)
print("Solución:")
print(solucion)


