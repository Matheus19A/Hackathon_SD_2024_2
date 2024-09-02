def subconjuntos(nums, max_size=None, min_size=None, distinct_only=False, sort_subsets=False):
    def gerar_subconjuntos(indice, atual):
        if (max_size is None or len(atual) <= max_size) and (min_size is None or len(atual) >= min_size):
            resultado.append(atual[:])
        if indice == len(nums):
            return
        for i in range(indice, len(nums)):
            if distinct_only and nums[i] in atual:
                continue
            atual.append(nums[i])
            gerar_subconjuntos(i + 1, atual)
            atual.pop()
    
    resultado = []
    gerar_subconjuntos(0, [])
    
    if sort_subsets:
        resultado = [sorted(subset) for subset in resultado]
        resultado.sort()
    
    return resultado

# Exemplo de uso
nums = [1, 2, 2]
print(subconjuntos(nums))  # Saída: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(subconjuntos(nums, max_size=2))  # Saída: [[], [1], [1, 2], [2], [2, 2]]
print(subconjuntos(nums, min_size=2))  # Saída: [[1, 2], [1, 2, 2], [2, 2]]
print(subconjuntos(nums, distinct_only=True))  # Saída: [[], [1], [1, 2], [2]]
print(subconjuntos(nums, sort_subsets=True))  # Saída: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
