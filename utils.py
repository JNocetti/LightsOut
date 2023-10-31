import numpy as np

def crearMatriz(filas, columnas):
    return np.random.randint(2, size=(filas, columnas))

def cambiarLuces(ai, aj, matriz):
    if (not existePosicion(ai, aj, matriz)):
        print("La posición no existe")
        return matriz
    else:
        if matriz[ai][aj] == 0:
            matriz[ai][aj] = 1
        else:
            matriz[ai][aj] = 0
    
    # Cambiar luz de arriba del seleccionado(ai, aj)
    if (existePosicion(ai, aj - 1, matriz)):
        if matriz[ai][aj - 1] == 0:
            matriz[ai][aj - 1] = 1
        else:
            matriz[ai][aj - 1] = 0
    # Cambiar luz de abajo del seleccionado(ai, aj)
    if (existePosicion(ai, aj + 1, matriz)):
        if matriz[ai][aj + 1] == 0:
            matriz[ai][aj + 1] = 1
        else:
            matriz[ai][aj + 1] = 0

    # Cambiar luz de la izquierda del seleccionado(ai, aj)
    if (existePosicion(ai - 1, aj, matriz)):
        if matriz[ai - 1][aj] == 0:
            matriz[ai - 1][aj] = 1
        else:
            matriz[ai - 1][aj] = 0

    # Cambiar luz de la derecha del seleccionado(ai, aj)
    if (existePosicion(ai + 1 , aj, matriz)):
        if matriz[ai + 1][aj] == 0:
            matriz[ai + 1][aj] = 1
        else:
            matriz[ai + 1][aj] = 0
    return matriz

def obtenerCambios(ai, aj, matriz):
    num_a_cambiar = []
    num_a_cambiar.append([ai, aj])
    # Cambiar luz de arriba del seleccionado(ai, aj)
    if (existePosicion(ai, aj - 1, matriz)):
        num_a_cambiar.append([ai, aj - 1])

    # Cambiar luz de abajo del seleccionado(ai, aj)
    if (existePosicion(ai, aj + 1, matriz)):
        num_a_cambiar.append([ai, aj + 1])

    # Cambiar luz de la izquierda del seleccionado(ai, aj)
    if (existePosicion(ai - 1, aj, matriz)):
        num_a_cambiar.append([ai - 1, aj])

    # Cambiar luz de la derecha del seleccionado(ai, aj)
    if (existePosicion(ai + 1 , aj, matriz)):
        num_a_cambiar.append([ai + 1, aj])
    return num_a_cambiar


def existePosicion(ai, aj, matriz):
    if (ai < matriz.shape[0] and ai >= 0 and aj < matriz.shape[1] and aj >= 0):
        return True
    else:
        return False
    
def convertirAX(matriz):
    matrizAX = np.full((matriz.shape[0], matriz.shape[1]), '  ')
    i = 0
    j = 0
    cont = 1
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            agregar = str('x' + str(cont))
            matrizAX[i][j] = agregar
            cont = cont + 1  
    return matrizAX

def devolverPosX(i, j, matrizAX):
    if (i < matrizAX.shape[0] and i >= 0 and j < matrizAX.shape[1] and j >= 0):
        return matrizAX[i][j]

def crearEcuaciones(matriz):
    matrizEcuaciones = []
    i = 0
    j = 0

    matrizAX = convertirAX(matriz)

    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            ecuacion = []
            strEcuacion = ''
            cambios = obtenerCambios(i, j,matriz)
            cantidad_cambios = len(cambios)
            for k in range(cantidad_cambios):
                c = cambios[k]
                pos1 = c[0]  # Guardar el primer valor en pos1
                pos2 = c[1]  # Guardar el segundo valor en pos2
                if(k + 1 < cantidad_cambios): 
                    strEcuacion += devolverPosX(pos1, pos2, matrizAX) + ' + '
                else:
                    strEcuacion += devolverPosX(pos1, pos2, matrizAX)
            strEcuacion += ' = ' + str(matriz[i][j])
            ecuacion = strEcuacion
            matrizEcuaciones.append(ecuacion)
    for num in range(len(matrizEcuaciones)):
        print(matrizEcuaciones[num] + "\n")
    return matrizEcuaciones