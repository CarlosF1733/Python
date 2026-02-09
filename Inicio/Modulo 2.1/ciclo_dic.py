import os
os.system('cls' if os.name == 'nt' else 'clear')

# Estrutura: { "Chave": Valor }
pauta = {
    "AL01": 16,
    "AL02": 8,
    "AL03": 12,
    "AL04": 19
}

# Em vez de .index(), vais direto ao assunto:
print(f"A nota do AL04 é: {pauta['AL04']}")

# 1. Adicionar um novo par
pauta["AL05"] = 20

# 2. Ver todas as chaves (os IDs)
print(f"Alunos: {list(pauta.keys())}")

# 3. Ver todos os valores (as notas)
print(f"Notas: {list(pauta.values())}")

# 4. O "Super For" para dicionários
for aluno, nota in pauta.items():
    print(f"O aluno {aluno} teve {nota} valores.")
