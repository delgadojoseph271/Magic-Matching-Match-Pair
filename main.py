from src.ux.pagina_de_inicio import menu_inicio
from src.motor import motor
from src.ux.pagina_final import pantalla_final
import pygame


def iniciar_juego():
    print("Iniciando el juego...")
    motor()

if __name__ == "__main__":
    # Iniciar la interfaz de usuario
    opcion = menu_inicio()
    if opcion == 'inicio':
        while True:
            final = motor()
            if final == 'salir':
                break
            if final== 'fin':
                opcion_final = pantalla_final()
                if opcion_final == 'reiniciar':
                    pass
                elif opcion_final=='salir':
                    break
            if opcion == 'salir':
                pass