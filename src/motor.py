from settings import ALTO, ANCHO, CLOCK, BLANCO,CELESTE
from utils.generarMatriz import generarMatriz
from utils.desordenarMatriz import desordenarMatriz
from utils.verificarCartasActivadas import verificarCartasActivadas
from utils.desactivarCartas import desactivarCartas
import pygame

def motor():
    pygame.init()
    # Maneja el tamaño de la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Matching Match Pair")

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
        pantalla.fill(CELESTE)

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
                return 'salir'
            if evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
                pos_mouse = pygame.mouse.get_pos()
                for fila in matriz_cartas:
                    for carta in fila:
                        if carta.colisionaConPuntos(pos_mouse=pos_mouse):
                            if len(pila) < 2:
                                if carta in pila:
                                    # Si la carta está en la pila, revertir estado
                                    if not carta.animando:
                                        carta.cambiarEstado()
                                        pila.clear()
                                else:
                                    if not carta.animando:
                                        carta.cambiarEstado()
                                        pila.append(carta)

                            if len(pila) == 2:
                                # Verificar si ambas cartas han terminado la animación
                                if not pila[0].animando and not pila[1].animando:
                                    if verificarCartasActivadas(pila):
                                        desactivarCartas(pila)
                                        pila.clear()
                                    else:
                                        # Si no coinciden, cambiar el estado de vuelta
                                        pila[0].cambiarEstado()
                                        pila[1].cambiarEstado()
                                        print('\n')
                                        print(pila[0].estado,pila[1].estado)
                                        pila.clear()

                            # Verificar si todas las cartas están activadas (se ha ganado)
                            if all([carta.estado for fila in matriz_cartas for carta in fila]):
                                print('¡Has ganado!')
                                juego_terminado = True
                                tiempo_final = tiempo_transcurrido  # Guardar el tiempo final
                                return 'fin'

        # Actualizar la pantalla
        pygame.display.update()
        CLOCK.tick(144)  # Aumentar el framerate para un cronómetro más fluido

motor()
