from src.ux.pagina_de_inicio import ux

def iniciar_juego():
    print("Iniciando el juego...")

if __name__ == "__main__":
    # Iniciar la interfaz de usuario
    ux()
opcion = ux()
if opcion == 'inicio':
    iniciar_juego()