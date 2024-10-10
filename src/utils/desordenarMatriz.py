import random

def desordenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    
    # Extraer los elementos de la matriz en una lista unidimensional
    elementos = [matriz[fila][columna] for fila in range(filas) for columna in range(columnas)]
    
    # Desordenar la lista de elementos
    random.shuffle(elementos)
    
    # Reasignar los elementos desordenados a la matriz original y actualizar las posiciones
    index = 0
    for i in range(filas):
        for j in range(columnas):
            carta = elementos[index]
            carta.rect.x = 100 + j * 120  # Actualiza la nueva posición x
            carta.rect.y = 100 + i * 160  # Actualiza la nueva posición y
            matriz[i][j] = carta
            index += 1

    return matriz
