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
    matrizAX = np.full((matriz.shape[0], matriz.shape[1]), '    ')
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
    # for num in range(len(matrizEcuaciones)):
    #     print(matrizEcuaciones[num])
    return matrizEcuaciones

def devolver_posicion_i_j(x):
    vector = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
    for i in range(len(vector)):
      if vector[i] == x:
        return i

def crearA_B(matriz, sistema_ecuaciones):
    A = np.zeros((len(sistema_ecuaciones), len(sistema_ecuaciones)))
    B = np.zeros((len(sistema_ecuaciones) , 1))

    

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
    
    # print("A")
    # print(A)


    # print("B") 
    # print(B)
    return A, B



def resolverJuego(matriz, sistema_ecuaciones):
    A, B = crearA_B(matriz, sistema_ecuaciones)
    
    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    AB = pivoteo_parcial(AB, n, m)
    AB1 = np.copy(AB)

    # eliminación hacia adelante (por filas)
    cont = 1
    for i in range(0,n-1,1):
        AB = pivoteo_parcial(AB,n, m)
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):  # k inicia de adelante hasta la últim fila avanzando fila por fila
            if(pivote!= 0):
                factor  = AB[k,i]/pivote
                AB = AB.astype(int)
                print(cont)
                cont = cont + 1
                AB[k,:] = (AB[k,:]) ^ (AB[i,:]* int(factor))

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):  # Para incluir el primera fila valor (0-1) en pasos de -1
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna] #valor de la matriz B en la fila i
        #X[i] = (b-suma)/AB[i,i]
        X[i] = (b - suma) % 2

    X = np.transpose([X])

    # SALIDA
    print(X)
    return X

def pivoteo_parcial(AB, n, m):
    # Pivoteo parcial por filas

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])  #todas las filas desde i hasta el final de la matriz y solo la columna i.
        dondemax = np.argmax(columna) #identifica la posición del elemento más grande en columna.

        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    return AB