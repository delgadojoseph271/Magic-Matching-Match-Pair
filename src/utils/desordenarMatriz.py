import random

def desordenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    elementos = [matriz[fila][columna] for fila in range(filas) for columna in range(columnas)]
    random.shuffle(elementos)
    
    # Reasignar los elementos desordenados a la matriz original
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = elementos.pop(0)

    return matriz