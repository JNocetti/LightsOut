import numpy as np

def crearMatriz(filas, columnas):
    return np.random.randint(2, size=(filas, columnas))

def resolver_lights_out(matriz_inicial):
    n = len(matriz_inicial)
    solucion = np.zeros((n, n), dtype=int)

    for fila in range(n):
        for columna in range(n):
            suma_vecinos = matriz_inicial[fila, columna]
            suma_vecinos += fila > 0 and matriz_inicial[fila - 1, columna]
            suma_vecinos += fila < n - 1 and matriz_inicial[fila + 1, columna]
            suma_vecinos += columna > 0 and matriz_inicial[fila, columna - 1]
            suma_vecinos += columna < n - 1 and matriz_inicial[fila, columna + 1]

            solucion[fila, columna] = suma_vecinos % 2

    return solucion.flatten()
    
