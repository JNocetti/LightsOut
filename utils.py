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
        print(matrizEcuaciones[num])
    return matrizEcuaciones

def devolver_posicion_i_j(x):
    vector = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
    for i in range(len(vector)):
      if vector[i] == x:
        return i

def crearA_B(matriz, sistema_ecuaciones):
    A = np.zeros((len(sistema_ecuaciones), len(sistema_ecuaciones)))
    B = np.zeros((9 , 1))

    

    for n_ecuacion in range(len(sistema_ecuaciones)):
        
        ecuacion = sistema_ecuaciones[n_ecuacion]
        #ecuacion = ecuacion.replace(" ", "")
        ecuacion =ecuacion.replace("+", "")
        parteIzquierda = ecuacion.split('=')
        cantidad_variables = len(parteIzquierda[0])
        cant_splits = cantidad_variables / 2
        cant_splits = int(cant_splits)
        partes_x = parteIzquierda[0].split(' ') 
        #for parte in partes_x:
            #if parte:
        partes_x = [parte for parte in parteIzquierda[0].split(' ') if parte]
 
        for i in range(len(partes_x)):  
            x = partes_x[i]  
            pos_i = n_ecuacion
            pos_j = devolver_posicion_i_j(x)  
            A[pos_i][pos_j] = 1 

        parteIzq = parteIzquierda[1].replace(" ", "")
        B[n_ecuacion] = int(parteIzq)
    
    print("A")
    print(A)


    print("B") 
    print(B)
    return A, B



def resolverJuego(matriz, sistema_ecuaciones):
    A, B = crearA_B(matriz, sistema_ecuaciones)
    
    # Matriz aumentada
    AB = np.concatenate((A, B), axis=1)
    n = A.shape[0]

    for i in range(n):
        # Encuentra el primer índice j con un 1 en la columna i
        j = i
        while j < n and AB[j, i] == 0:
            j += 1
        
        # Si no se encontró un 1, sigue con la siguiente columna
        if j == n:
            continue
        
        # Intercambia filas para tener el 1 en la posición (i, i)
        AB[[i, j]] = AB[[j, i]]

        # Realiza eliminación hacia adelante
        for k in range(n):
            if k != i:
                factor = AB[k, i] / AB[i, i]
                AB[k, :] -= factor * AB[i, :]

    # Normaliza las filas para que los elementos diagonales sean 1
    for i in range(n):
        if AB[i, i] != 0:
            AB[i, :] /= AB[i, i]

    # Obtiene la solución como un vector de 0 y 1
    solucion = [1 if valor > 0.5 else 0 for valor in AB[:, -1]]

    return solucion
