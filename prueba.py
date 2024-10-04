import pygame
import sys
import os
from settings import ANCHO, ALTO, FPS, AMARILLO, ROSADO,BLANCO,CELESTE,CLOCK,VERDECITO,MORADO
from elementos import Boton
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Pantalla de Inicio")
#funciones para los botones

def salir_juego(): 
    pygame.quit()
    sys.exit()
#crear botones
boton_iniciar= Boton(300, 200, 200, 50, "Jugar", ROSADO, MORADO, )
boton_salir = Boton(300, 300, 200, 50, "Salir", ROSADO, MORADO, salir_juego )

#bucle 
def menu_inicio():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Pantalla de Inicio")
    corriendo = True
    while corriendo:
        pantalla.fill(AMARILLO)
    #dibuja los botones 
        boton_iniciar.draw(pantalla)
        boton_salir.draw(pantalla)
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                corriendo= False
            if boton_salir.is_clicked(evento):
                salir_juego()  
        pygame.display.update()
        CLOCK.tick(3)
    pygame.quit()
    sys.exit()
if __name__=="__main__":   
    menu_inicio()   


