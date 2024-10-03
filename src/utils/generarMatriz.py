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
    urls = [os.path.join(directorio, archivo) for archivo in archivos]
    
    # Mezcla las URLs para obtener aleatoriedad
    random.shuffle(urls)
    
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