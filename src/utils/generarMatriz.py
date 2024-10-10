import pygame
import sys
import os
import random
# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.objetos import cartas
from src.settings import ROJO

def generarMatriz(pantalla, filas, columnas):
    directorio = 'img/imagenes volteadas'
    archivos = os.listdir(directorio)
    
    # Verifica que tengas suficientes imágenes para crear los pares
    cantidad_cartas = filas * columnas
    if cantidad_cartas % 2 != 0:
        raise ValueError("El número de cartas debe ser par para formar pares iguales.")
    
    # Tomamos suficientes imágenes para llenar la matriz (mitad de la cantidad total de cartas)
    archivos_seleccionados = archivos[:cantidad_cartas // 2]
    
    # Duplicamos las imágenes para tener pares
    pares_imagenes =  [archivo for archivo in archivos_seleccionados for _ in range(2)]
    
    # Mezclamos los pares para que no estén uno junto al otro
    
    # Crea las URLs para cada imagen seleccionada
    urls = [os.path.join(directorio, archivo) for archivo in pares_imagenes]
    # Crea la matriz
    matriz = [[cartas(
                pantalla, 
                valor=fila, 
                color=ROJO, 
                posicion=(100 + columna * 120, 100 + fila * 160),
                img=urls.pop() if urls else None  # Evita errores si se acaban las imágenes
                ) for columna in range(columnas)] 
                    for fila in range(filas)]
    
    return matriz