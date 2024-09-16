from settings import ALTO, ANCHO, CLOCK, BLANCO, ROJO, AZUL, NEGRO

from utils.generarMatriz import  generarMatriz
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

    # Crear la matriz de cartas
    matriz_cartas = generarMatriz(pantalla=pantalla, filas=FILAS, columnas=COLUMNAS)
    #desordenar una matriz
    matriz_cartas = desordenarMatriz(matriz_cartas) #de momento nose porque no lo desordena
    # Ciclo principal del juego
    corriendo = True
    while corriendo:
        # Pintar la pantalla de blanco 
        pantalla.fill(BLANCO)
        # Dibujar la matriz de cartas
        for fila in matriz_cartas:
            for carta in fila:
                carta.dibujar()

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del clic
                pos_mouse = pygame.mouse.get_pos()
                
                # Verificar si alguna carta fue clickeada
                for fila in matriz_cartas:
                    for carta in fila:
                        if carta.colisionaConPuntos(pos_mouse=pos_mouse):
                            carta.cambiarEstado()
                            #necesito una funcion que cree una pila de 2 elementos si los valores no son iguales los vuelve false

        # Verificar las cartas activadas
        valor_pares, cartas_activadas = verificarCartasActivadas(matriz_cartas)
        if valor_pares is not None:
            print(f"Hay al menos 2 cartas activadas con el valor: {valor_pares}")
            desactivarCartas(matriz_cartas, valor_pares)
        else:
            print("No hay pares de cartas activadas con el mismo valor.")

        # Actualizar la pantalla
        pygame.display.update()
        CLOCK.tick(60)

motor()
