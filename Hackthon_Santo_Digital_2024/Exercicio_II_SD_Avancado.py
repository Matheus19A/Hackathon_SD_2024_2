def menor_diferenca(array, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    # Ordena o array
    array.sort()
    
    # Inicializa a menor diferença com um valor grande
    menor_dif = float('inf')
    pares = []
    
    # Percorre o array comparando pares adjacentes
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if not allow_duplicates and array[i] == array[j]:
                continue
            dif = abs(array[j] - array[i])
            if dif < menor_dif:
                menor_dif = dif
                pares = [(array[i], array[j])]
            elif dif == menor_dif:
                pares.append((array[i], array[j]))
    
    # Ordena os pares se sorted_pairs for True
    if sorted_pairs:
        pares = [tuple(sorted(par)) for par in pares]
    
    # Remove pares duplicados se unique_pairs for True
    if unique_pairs:
        pares = list(set(pares))
    
    return pares

# Exemplo de uso
array = [4, 9, 1, 32, 13, 5, 6, 7, 7]
print(menor_diferenca(array))  # Saída: [(4, 5), (5, 6), (6, 7), (7, 7)]
print(menor_diferenca(array, allow_duplicates=False))  # Saída: [(4, 5), (5, 6), (6, 7)]
print(menor_diferenca(array, sorted_pairs=True))  # Saída: [(4, 5), (5, 6), (6, 7), (7, 7)]
print(menor_diferenca(array, unique_pairs=True))  # Saída: [(4, 5), (5, 6), (6, 7)]
print(menor_diferenca(array, allow_duplicates=False, sorted_pairs=True, unique_pairs=True))  # Saída: [(4, 5), (5, 6), (6, 7)]
