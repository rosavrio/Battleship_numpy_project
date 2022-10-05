import numpy as np
import random
from funciones import *

#importamos funciones que dan error desde el modulo funciones.py

def dispara_jugador(fila, col):
    if tablero_maquina[fila,col] == ' ':
        tablero_maquina[fila, col] = 'A'
    elif tablero_maquina[fila, col] == '1':
        tablero_maquina[fila,col] = 'X'
        
    return tablero_maquina



def disparar_maquina():      
    coord = random.choice(lista_posiciones)
    if tablero_jugador[coord[0], coord[1]] == ' ':
        tablero_jugador[coord[0], coord[1]] = 'A'
    else:
        tablero_jugador[coord[0], coord[1]] = 'X'

    lista_posiciones.remove(coord)
    return tablero_jugador, print(tablero_jugador)


# creamos una lista de tuplas con las posiciones posibles a las que la maquina puede disparar
lista_posiciones = []

for x in range(0,10): # se rellena con este bucle
    for i in range(0,10):
        lista_posiciones.append(tuple((x,i)))

# para evitar errores delimitamos los posibles inputs de coordenadas
posiciones_validas = (0,1,2,3,4,5,6,7,8,9)


# Creamos los tableros y mostramos el tablero del jugador, pero no el de la maquina
tablero_maquina = Tablero()
tablero_maquina.tablero

print('Tablero máquina')
tablero_maquina = tablero_maquina.colocar_barcos_random()


tablero_jugador = Tablero()
tablero_jugador.tablero

print('Tu tablero')
tablero_jugador = tablero_jugador.colocar_barcos_manual()
print(tablero_jugador)

# aqui generamos el bucle del juego
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