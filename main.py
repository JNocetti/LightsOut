import numpy as np
import utils

# filas = int(input("Ingrese el número de filas: "))
# columnas = int(input("Ingrese el número de columnas: "))
filas = 3
columnas = 3
matriz = utils.crearMatriz(filas, columnas)



print(matriz)
ecuaciones = utils.crearEcuaciones(matriz)
# cambiar = input("Presione C para cambiar luces: ")
# while (cambiar == "C" or cambiar == "c"):
#     ai = int(input("Ingrese la fila del elemento: "))
#     aj = int(input("Ingrese la columna del elemento: "))
#     matriz = utils.cambiarLuces(ai, aj, matriz)
#     print(matriz)
#     cambiar = input("Presione C para cambiar luces o cualquier tecla para salir: ")
solucion =  utils.resolver_sistema_lights_out( matriz)
print(solucion)