import numpy as np
import utils

filas = 3
columnas = 3
matriz = utils.crearMatriz(filas, columnas)

print("Matriz de luces: ")
print(matriz)

print("Ecuaciones: ")
ecuaciones = utils.crearEcuaciones(matriz)

solucion = utils.resolverJuego(matriz,ecuaciones)
print("Solución del juego: ")
print(solucion)