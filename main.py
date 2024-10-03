from src.ux.pagina_de_inicio import PaginaInicio
from src.motor import motor

def iniciar_juego():
    print("Iniciando el juego...")

if __name__ == "__main__":
    # Iniciar la interfaz de usuario
    opcion = PaginaInicio()
if opcion == 'inicio':
    motor()