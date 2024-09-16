import pygame
# archivo: src/ux/pagina_de_inicio.py
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.settings import ANCHO, ALTO, FPS, BLANCO, ROJO

# Resto del código

def ux():
    # Código para la UX aquí...
    opcion_seleccionada = 'inicio'
    # Retorna una opción seleccionada
    return opcion_seleccionada

