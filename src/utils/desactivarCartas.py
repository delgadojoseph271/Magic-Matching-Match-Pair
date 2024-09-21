def desactivarCartas(matriz):
    for carta in matriz:
            if carta.valor:
                carta.clickeable = False  # Desactiva la capacidad de ser clickeada