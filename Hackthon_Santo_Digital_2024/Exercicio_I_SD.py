def gerar_asteriscos(n):
    return ['*' * i for i in range(1, n + 1)]

# Exemplo de uso
n = 9
print(gerar_asteriscos(n))  # Saída: ['*', '**', '***', '****', '*****']
