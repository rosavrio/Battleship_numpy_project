import numpy as np
import random
from funciones import *

lista_posiciones = []

for x in range(0,10): # se rellena con este bucle
    for i in range(0,10):
        lista_posiciones.append(tuple((x,i)))

posiciones_validas = (0,1,2,3,4,5,6,7,8,9)

tablero_maquina = Tablero()
tablero_maquina.tablero

print('Tablero máquina')
tablero_maquina = tablero_maquina.colocar_barcos_random()
print(tablero_maquina)


tablero_jugador = Tablero()
tablero_jugador.tablero

print('Tu tablero')
tablero_jugador = tablero_jugador.colocar_barcos_manual()
print(tablero_jugador)


while '1' in tablero_jugador or '1' in tablero_maquina:
    tablero_jugador
    tablero_maquina
    
    fila = int(input('Coordenada fila'))
    col = int(input('Coordenada columna'))
   
    dispara_jugador(fila, col)
    disparar_maquina()

    if '1' not in tablero_jugador or '1' not in tablero_maquina:
        print('El juego ha terminado.')
        if '1' not in tablero_jugador:
            print('La máquina ha ganado.')
            break
        else:
            print('Enhorabuena, has ganado la partida.')
            break