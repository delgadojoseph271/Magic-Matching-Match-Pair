def verificarCartasActivadas(matriz):
    conteo_valores = {}
    cartas_activadas = [] # es una pila de 2

    # Recorrer la matriz para contar las cartas activadas por valor
    for fila in matriz:
        for carta in fila:
            if carta.estado:  # Si la carta está activada
                if carta.valor in conteo_valores:
                    conteo_valores[carta.valor] += 1
                    cartas_activadas.append(carta)  # Guardar carta activada
                else:
                    conteo_valores[carta.valor] = 1
                    cartas_activadas.append(carta)  # Guardar carta activada
    
    # Verificar si hay algún valor con 2 o más cartas activadas
    valor_pares = None
    for valor, conteo in conteo_valores.items():
        if conteo >= 2:
            valor_pares = valor
            break
    
    return valor_pares, cartas_activadas