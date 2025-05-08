import numpy as np
import time
import random

# Función para crear tablero
def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


# barco_jugador = [[[1,6], [2,6], [3,6], [4,6]], [[0,1], [1,1], [2,1]], [[1,0], [2,0], [3,0]],[[1,9], [2,9]], [[5,0], [6,0]], [[1,5], [2,5]]]
# barco_rival = [[[0,1], [0,2], [0,3], [0,4]], [[1,1], [1,2], [1,3]], [[3,1], [4,1], [5,1]],[[1,5], [2,5]], [[5,3], [5,4]], [[7,0], [8,0]]]

# Función para colocar barcos jugador

def colocar_barcos(tablero, barcos):
   
    for  i in barcos:
        for j in i:
            tablero[j[0], j[1]] = "O"
        
    return tablero

def disparo(tablero, fila, columna):
   
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        print("¡¡¡IMPACTOOOOO!!!")
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posicion ya seleccionada")
        disparo()
    else:
        tablero[fila,columna] = "#"
        print("FALLASTE :)")
    return tablero

def disparo_2(tablero, fila, columna):
    tablero[fila, columna]= "X"
    return tablero