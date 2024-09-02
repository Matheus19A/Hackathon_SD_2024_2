def menor_diferenca(array):
    # Ordena o array
    array.sort()
    
    # Inicializa a menor diferença com um valor grande
    menor_dif = float('inf')
    pares = []
    
    # Percorre o array comparando pares adjacentes
    for i in range(len(array) - 1):
        dif = array[i + 1] - array[i]
        if dif < menor_dif:
            menor_dif = dif
            pares = [(array[i], array[i + 1])]
        elif dif == menor_dif:
            pares.append((array[i], array[i + 1]))
    
    return pares

# Exemplo de uso
array = [4, 9, 1, 32, 13, 5, 6, 7]
print(menor_diferenca(array))  # Saída: [(4, 5), (5, 6), (6, 7)]
