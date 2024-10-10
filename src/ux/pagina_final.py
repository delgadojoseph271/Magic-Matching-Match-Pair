import pygame
import sys
import os


# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.settings import ANCHO, ALTO, CLOCK, ROSADO, MORADO
from src.Boton import Boton

# Ruta de la imagen de fondo
fondo_path = os.path.join('img/fondo_final.png')
fondo = pygame.image.load(fondo_path)

# Función para la pantalla final
def pantalla_final():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Pantalla Final")
    boton_reiniciar = Boton(300, 200, 200, 50, "Volver a jugar", ROSADO, MORADO)
    boton_salir = Boton(300, 300, 200, 50, "Salir", ROSADO, MORADO)
    corriendo = True

    while corriendo:
        pantalla.blit(fondo, (0, 0))
        
        # Dibujar los botones
        boton_reiniciar.dibujar(pantalla)
        boton_salir.dibujar(pantalla)
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                corriendo = False
            if boton_reiniciar.es_clicleado(evento):
                return 'inicio'
            if boton_salir.es_clicleado(evento):
                return 'salir'
        pygame.display.update()
        CLOCK.tick(3)
    pygame.quit()
    sys.exit()

pantalla_final()