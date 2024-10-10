from settings import ALTO, ANCHO, CLOCK, BLANCO, ROJO, AZUL, NEGRO
from utils.generarMatriz import generarMatriz
from utils.desordenarMatriz import desordenarMatriz
from utils.verificarCartasActivadas import verificarCartasActivadas
from utils.desactivarCartas import desactivarCartas
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
                #print('se dibujo')
        #print('.')
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
                                if carta in pila:
                                    print('antes: ',carta.estado)
                                    carta.cambiarEstado()
                                    print('depues: ',carta.estado)
                                    pila.clear()
                                    print('limpio')
                                    print(pila)
                                else:
                                    pila.append(carta)
                                    print('antes desde else linia 69:  ',carta.estado)
                                    carta.cambiarEstado()
                                    print('depues desde else linia 71: ',carta.estado)
                                    print('objetos de la pila linia 72',pila)
                                    print('tamano de la pila linia 73',len(pila))
                                    
                            
                            
                            if len(pila) == 2:
                                print('estados de carta linia 78' ,pila[0].estado,pila[1].estado)
                                if verificarCartasActivadas(pila):
                                    desactivarCartas(pila)
                                    pila.clear()
                                else:
                                    print('entro al else')
                                    pila[0].cambiarEstado()
                                    pila[1].cambiarEstado()
                                    print(pila[0].estado,pila[1].estado)
                                    pila.clear()
                                    print(pila)

                            # Verificar si todas las cartas están activadas (se ha ganado)
                            print(([carta.estado for fila in matriz_cartas for carta in fila]))
                            if all([carta.estado for fila in matriz_cartas for carta in fila]):
                                print('¡Has ganado!')
                                juego_terminado = True
                                tiempo_final = tiempo_transcurrido  # Guardar el tiempo final
                            print('\n terminacion del ciclo \n')

        # Actualizar la pantalla
        pygame.display.update()
        CLOCK.tick(144)  # Aumentar el framerate para un cronómetro más fluido

motor()
