from src.settings import ALTO, ANCHO, CLOCK, BLANCO, ROJO, AZUL, NEGRO
from src.utils.generarMatriz import generarMatriz
from src.utils.desordenarMatriz import desordenarMatriz
from src.utils.verificarCartasActivadas import verificarCartasActivadas
from src.utils.desactivarCartas import desactivarCartas
import pygame

def motor():
    pygame.init()
    # Maneja el tamaño de la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Detección de Clic")

    # Dimensiones de la matriz
    COLUMNAS = 2
    FILAS = 3

    # Crear y desordenar la matriz de cartas
    matriz_cartas = generarMatriz(pantalla=pantalla, filas=FILAS, columnas=COLUMNAS)
    matriz_cartas = desordenarMatriz(matriz_cartas)

    pila = []  # Pila de cartas seleccionadas
    corriendo = True

    # Temporizador
    fuente = pygame.font.SysFont('Consolas', 20)
    tiempo_inicio = pygame.time.get_ticks()  # Tiempo de inicio del juego
    juego_terminado = False
    tiempo_final = None

    while corriendo:
        pantalla.fill(BLANCO)

        # Obtener tiempo transcurrido
        if not juego_terminado:
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = (tiempo_actual - tiempo_inicio) / 1000  # En segundos
        else:
            tiempo_transcurrido = tiempo_final

        # Mostrar cronómetro
        texto_tiempo = fuente.render(f'Tiempo: {tiempo_transcurrido:.2f} s', True, (0, 0, 255))
        pantalla.blit(texto_tiempo, (10, 10))  # Dibujar el cronómetro en la pantalla

        # Dibujar la matriz de cartas
        for fila in matriz_cartas:
            for carta in fila:
                carta.dibujar()

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
                pos_mouse = pygame.mouse.get_pos()
                for fila in matriz_cartas:
                    for carta in fila:
                        if carta.colisionaConPuntos(pos_mouse=pos_mouse):
                            if len(pila) < 2:
                                pila.append(carta)
                                print(pila)
                                print(len(pila))

                            carta.cambiarEstado()
                            if len(pila) == 2:
                                if verificarCartasActivadas(pila):
                                    desactivarCartas(pila)
                                    pila.clear()
                                else:
                                    pila[1].dibujar()
                                    pila[0].resetear()
                                    pila[1].resetear()
                                    pila.clear()

                            # Verificar si todas las cartas están activadas (se ha ganado)
                            if all([carta.estado for fila in matriz_cartas for carta in fila]):
                                print('¡Has ganado!')
                                juego_terminado = True
                                tiempo_final = tiempo_transcurrido  # Guardar el tiempo final
                                

        # Actualizar la pantalla
        pygame.display.update()
        CLOCK.tick(3)  # Aumentar el framerate para un cronómetro más fluido

#motor()
