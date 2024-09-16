def marcarCartasPares(matriz, valor_pares):
    for fila in matriz:
        for carta in fila:
            if carta.valor == valor_pares:
                carta.no_cambiar_estado = True  # Marcar como parte de un par