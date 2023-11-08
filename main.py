import tkinter as tk
from tkinter import ttk
import numpy as np
import utils
from PIL import Image, ImageTk
from tkinter import messagebox

canvas = None
ancho_celda = 0
altura_celda = 0
ventana_matriz = None
matriz = [] 

def ver_solucion():  
    if(len(matriz) != 0):
        print(matriz)
        ecuaciones = utils.crearEcuaciones(matriz)
        solucion = utils.resolverJuego(matriz, ecuaciones)
        texto_resultado.set(f"La solución es: {solucion}")
    else:
        messagebox.showinfo("Error", "Primero debes generar una matriz")

def generar_matriz():
    global matriz
    filas = int(entry_filas.get())
    columnas = int(entry_columnas.get())
    matriz = utils.crearMatriz(filas, columnas)
    mostrar_matriz(matriz) 

def mostrar_matriz(matriz):
    global canvas, ancho_celda, altura_celda, ventana_matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    if canvas is None:
        ancho_ventana = 600
        altura_ventana = 600

        ventana_matriz = tk.Toplevel()
        ventana_matriz.title("Matriz")
        ventana_matriz.geometry(f"{ancho_ventana}x{altura_ventana}")

        ancho_celda = ancho_ventana // columnas
        altura_celda = altura_ventana // filas

        canvas = tk.Canvas(ventana_matriz, width=ancho_ventana, height=altura_ventana)
        canvas.pack()

    for i in range(filas):
        for j in range(columnas):
            x0 = j * ancho_celda
            y0 = i * altura_celda
            x1 = x0 + ancho_celda
            y1 = y0 + altura_celda

            color = 'green' if matriz[i][j] == 1 else 'red'
            cell = canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    canvas.bind("<Button-1>", on_cell_click)

def on_cell_click(event):
    global canvas, ancho_celda, altura_celda, matriz  # Asegurarse de usar las variables globales

    widget = event.widget
    x, y = widget.canvasx(event.x), widget.canvasy(event.y)
    col = int(x // ancho_celda)
    fila = int(y // altura_celda)

    nueva_matriz = utils.cambiarLuces(fila, col, matriz)
    actualizar_matriz(nueva_matriz)

    if all_zeroes(nueva_matriz):
        messagebox.showinfo("Fin del juego", "¡Has ganado, todas las luces están apagadas!")
        canvas.unbind("<Button-1>")

def actualizar_matriz(nueva_matriz):
    global canvas, ventana_matriz, matriz
    canvas.delete("all")
    matriz = nueva_matriz
    mostrar_matriz(nueva_matriz)

def all_zeroes(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento != 0:
                return False
    return True

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

