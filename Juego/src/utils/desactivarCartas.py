def desactivarCartas(matriz, valor_pares):
    for fila in matriz:
        for carta in fila:
            if carta.valor != valor_pares:
                carta.estado = False  # Desactivar cartas que no coinciden
