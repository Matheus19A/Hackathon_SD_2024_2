def subconjuntos(nums):
    # Função recursiva para gerar subconjuntos
    def gerar_subconjuntos(indice, atual):
        if indice == len(nums):
            resultado.append(atual[:])
            return
        # Inclui o elemento atual no subconjunto
        atual.append(nums[indice])
        gerar_subconjuntos(indice + 1, atual)
        # Exclui o elemento atual do subconjunto
        atual.pop()
        gerar_subconjuntos(indice + 1, atual)
    
    resultado = []
    gerar_subconjuntos(0, [])
    return resultado

# Exemplo de uso
nums = [1, 2]
print(subconjuntos(nums))  # Saída: [[], [1], [2], [1, 2]]
