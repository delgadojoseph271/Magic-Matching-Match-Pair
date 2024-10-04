from src.ux.pagina_de_inicio import menu_inicio
from src.motor import motor


def iniciar_juego():
    print("Iniciando el juego...")
    motor()

if __name__ == "__main__":
    # Iniciar la interfaz de usuario
    opcion = menu_inicio()
    if opcion == 'inicio':
        motor()
    if opcion == 'salir':
        pass