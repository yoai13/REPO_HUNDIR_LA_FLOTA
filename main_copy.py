import utils_copy
import variables_copy as vr
import random
import time


tablero_rival_barcos = utils_copy.crear_tablero()    # MOSTRAR BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.
tablero_rival_disparos = utils_copy.crear_tablero()  # MOSTRAR DISPAROS DEL RIVAL.

tablero_jugador_barcos = utils_copy.crear_tablero()  # MOSTRAR BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL.
tablero_jugador_disparos = utils_copy.crear_tablero()    # MOSTRAR DISPAROS DEL JUGADOR.


tablero_rival_barcos = utils_copy.colocar_barcos(tablero_rival_barcos, vr.barco_rival) 
tablero_jugador_barcos = utils_copy.colocar_barcos(tablero_jugador_barcos, vr.barco_jugador)

print("Bienvenidos a Jugar la Flota")

print("TE MUESTRO LOS TABLEROS")

print("_"*75)

print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.")
print(tablero_rival_barcos)

print("_"*75)

print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL RIVAL")
print(tablero_rival_disparos)

print("_"*75)

print("TABLERO DONDE SE MUESTRA LOS BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL")
print(tablero_jugador_barcos)

print("_"*75)

print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL JUGADOR.")
print(tablero_jugador_disparos)

print("_"*75)

turno=1
while True:
    if turno==1: # ESTO SIGNIFICA QUE ES EL TURNO DEL JUGADOR
        print("ES TU TURNO")
        fila=int(input("SELECCIONA LA FILA CON UN MUMERO DEL 0 AL 9: "))
        columna=int(input("SELECCIONA LA COLUMNA CON UN MUMERO DEL 0 AL 9: "))
        tablero_jugador_disparos=utils_copy.disparo_2(tablero_jugador_disparos, fila, columna)
        tablero_rival_barcos=utils_copy.disparo(tablero_rival_barcos, fila, columna)
        print("_"*75)
        print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL JUGADOR")
        print(tablero_jugador_disparos)
        print("_"*75)
        print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR")
        print(tablero_rival_barcos)
        turno=0 # AQUI CAMBIA EL TURNO AL RIVAL


        barco_hundido =all("O" not in fila for fila in tablero_rival_barcos)
        if barco_hundido:
            print("HAS GANADO LA PARTIDA")
            break

    else:
        print("TURNO DEL RIVAL")
        fila = random.randint(0,9)
        columna = random.randint(0,9)

        tablero_rival_disparos=utils_copy.disparo_2(tablero_rival_disparos, fila, columna)
        tablero_jugador_barcos=utils_copy.disparo(tablero_jugador_barcos, fila, columna)

        print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL RIVAL")
        print(tablero_rival_disparos)
        print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL")
        print(tablero_jugador_barcos)
        turno=1 # VOLVERIA A CAMBIAR DE TURNO






PendingDeprecationWarning
