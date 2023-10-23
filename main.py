import numpy as np
import utils

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = utils.crearMatriz(filas, columnas)

print(matriz)
