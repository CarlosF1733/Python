import os
os.system('cls' if os.name == 'nt' else 'clear')

notas = [5, 12, 16, 8, 19, 20]

# 1. Encontrar o maior e o menor valor da lista completa
nota_mais_alta = max(notas)
nota_mais_baixa = min(notas)

print(f"A maior nota da lista é: {nota_mais_alta}")
print(f"A menor nota da lista é: {nota_mais_baixa}")

# 2. Se quiseres fazer isto apenas no Slicing (excluindo a primeira e última)
notas_reais = notas[1:-1]
print(f"\nNas notas reais {notas_reais}:")
print(f"O máximo é {max(notas_reais)} e o mínimo é {min(notas_reais)}")