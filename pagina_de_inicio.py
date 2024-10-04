import pygame
import sys
import os
from settings import ANCHO, ALTO, FPS, AMARILLO, ROSADO,BLANCO,CELESTE,CLOCK,VERDECITO,MORADO
from elementos import Boton
from src.motor import motor
pygame.init
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Pantalla de Inicio")
#funciones para los botones
def iniciar_juego():
    motor() #Llama a al motor para iniciar el juego 
def salir_juego(): 
    pygame.quit()
    sys.exit()
#crear botones
boton_iniciar= Boton(300, 200, 200, 50, "Jugar", ROSADO, MORADO, iniciar_juego)
boton_salir = Boton(300, 300, 200, 50, "Salir", ROSADO, MORADO, salir_juego )

#bucle 
def menu_inicio():
    corriendo = True
    while corriendo:
        pantalla.fill(AMARILLO)
    #dibuja los botones 
    boton_iniciar.draw(pantalla)
    boton_salir.draw(pantalla)
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            corriendo= False
        if boton_iniciar.is_clicked(evento):
            iniciar_juego
        if boton_salir.is_clicked(evento):
            salir_juego()       

