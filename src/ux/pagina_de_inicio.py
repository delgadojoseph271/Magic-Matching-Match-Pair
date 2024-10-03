import pygame
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path ANTES de importar otros módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importaciones personalizadas
from src.utils.Boton import Boton
from src.settings import ANCHO, ALTO, FPS, BLANCO, ROJO, AZUL

# Resto del código

def PaginaInicio():
    # Código para la UX aquí...
    pygame.init()
    # Maneja el tamaño de la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Detección de Clic")
    opcion_seleccionada = 'inicio'

    boton_inicio = Boton(300, 250, 200, 60, AZUL, "Iniciar")
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            
            # Detecta si se hizo clic en el botón
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_inicio.es_presionado(evento.pos):
                    opcion_seleccionada = 'inicio'
                    return opcion_seleccionada
        
        # Rellena la pantalla con blanco
        pantalla.fill(BLANCO)

        # Dibuja el botón
        boton_inicio.dibujar(pantalla)
        

        # Actualiza la pantalla
        pygame.display.flip()

        # Retorna una opción seleccionada

PaginaInicio()
