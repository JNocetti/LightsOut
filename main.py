# import numpy as np
# import utils

# # filas = int(input("Ingrese el número de filas: "))
# # columnas = int(input("Ingrese el número de columnas: "))
# filas = 3
# columnas = 3
# matriz = utils.crearMatriz(filas, columnas)




# print("Matriz de luces: ")
# print(matriz)

# # print("Ecuaciones: ")
# ecuaciones = utils.crearEcuaciones(matriz)

# # print("Matriz A y B: ")
# xayb = utils.crearA_B(matriz, ecuaciones)

# print("Solución: ")
# solucion = utils.resolverJuego(matriz, ecuaciones)

# cambiar = input("Presione C para cambiar luces: ")
# while (cambiar == "C" or cambiar == "c"):
#     ai = int(input("Ingrese la fila del elemento: "))
#     aj = int(input("Ingrese la columna del elemento: "))
#     matriz = utils.cambiarLuces(ai, aj, matriz)
#     print(matriz)
#     cambiar = input("Presione C para cambiar luces o cualquier tecla para salir: ")
    


import tkinter as tk
from tkinter import ttk
import numpy as np
import utils
from PIL import Image, ImageTk

matriz = []

def ver_solucion():
    print(matriz)
    ecuaciones = utils.crearEcuaciones(matriz)
    solucion = utils.resolverJuego(matriz, ecuaciones)
    texto_resultado.set(f"La solución es: {solucion}")

def generar_matriz():
    global matriz
    filas = int(entry_filas.get())
    columnas = int(entry_columnas.get())
    matriz = utils.crearMatriz(filas, columnas)
    # texto_matriz.set(str(matriz))
    mostrar_matriz(matriz)

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    ancho_celda = 100
    altura_celda = 100
    grosor_linea = 3  # Grosor de la línea divisoria

    ancho_ventana = ancho_celda * columnas
    altura_ventana = altura_celda * filas

    ventana_matriz = tk.Toplevel()
    ventana_matriz.title("Matriz")
    ventana_matriz.geometry(f"{ancho_ventana}x{altura_ventana}+600+100")

    canvas = tk.Canvas(ventana_matriz, width=ancho_ventana, height=altura_ventana)
    canvas.pack()

    for i in range(filas):
        for j in range(columnas):
            x0 = j * ancho_celda
            y0 = i * altura_celda
            x1 = x0 + ancho_celda
            y1 = y0 + altura_celda

            color = 'green' if matriz[i][j] == 1 else 'red'
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=grosor_linea)

            # Agregar el valor de la celda en el centro
            canvas.create_text(x0 + ancho_celda // 2, y0 + altura_celda // 2, text=str(matriz[i][j]))



ventana = tk.Tk()
ventana.title("Lights out")
ventana.geometry("800x500")  # Tamaño de la ventana

# Título
titulo = tk.Label(ventana, text="Lights out", font=("Arial", 16, "bold"))
titulo.pack()

# Texto introductorio
texto_intro = tk.Label(ventana, text="¡Bienvenido! Introduce las filas y columnas para generar la matriz.")
texto_intro.pack()

# Entradas para filas y columnas
label_filas = tk.Label(ventana, text="Filas:", justify=tk.RIGHT)
label_filas.pack()
entry_filas = tk.Entry(ventana)
entry_filas.pack()

label_columnas = tk.Label(ventana, text="Columnas:",  justify=tk.RIGHT)
label_columnas.pack()
entry_columnas = tk.Entry(ventana)
entry_columnas.pack()

# Botón para generar la matriz
boton_generar = tk.Button(ventana, text="Generar matriz", command=generar_matriz)
boton_generar.pack()

# Mostrar matriz
texto_matriz = tk.StringVar()
label_matriz = tk.Label(ventana, textvariable=texto_matriz)
label_matriz.pack()

# Botón para ver solución
boton_solucion = ttk.Button(ventana, text="Ver solución", command=ver_solucion)
boton_solucion.pack()

# Mostrar texto de resultado
texto_resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=texto_resultado)
label_resultado.pack()

ventana.mainloop()

