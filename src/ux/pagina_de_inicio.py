import pygame
# archivo: src/ux/pagina_de_inicio.py
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.settings import ANCHO, ALTO, FPS, AMARILLO, ROSADO,BLANCO,CELESTE,CLOCK,VERDECITO,MORADO
from src.Boton import Boton

# Resto del código
    # Código para la UX aquí...
    #crear botones

#bucle 
#imagen
#imagen
fondo_path= os.path.join('img/LOL.png')
fondo= pygame.image.load(fondo_path)
#bucle 
def menu_inicio():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Pantalla de Inicio")
    boton_iniciar= Boton(300, 200, 200, 50, "Jugar", ROSADO, MORADO)
    boton_salir = Boton(300, 300, 200, 50, "Salir", ROSADO, MORADO)
    corriendo = True
    while corriendo:
        pantalla.blit(fondo,(0,0))
    #dibuja los botones 
        boton_iniciar.dibujar(pantalla)
        boton_salir.dibujar(pantalla)
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                corriendo = False
            if boton_iniciar.es_clicleado(evento):
                return 'inicio'
            if boton_salir.es_clicleado(evento):
                return 'salir'
        pygame.display.update()
        CLOCK.tick(3)
    pygame.quit()
    sys.exit()
        # Retorna una opción seleccionada

