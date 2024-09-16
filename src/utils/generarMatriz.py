import pygame
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.objetos import cartas
from src.settings import ROJO, AZUL

def generarMatriz(pantalla, filas, columnas):
    color = ROJO if cartas.estado == False else AZUL
    matriz = [[cartas(pantalla, valor=fila, color=color, posicion=(100 + columna * 60, 100 + fila * 80)) for columna in range(columnas)] for fila in range(filas)]
    return matriz