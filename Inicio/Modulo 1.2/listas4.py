import os
os.system('cls' if os.name == 'nt' else 'clear')

# Uma LISTA de DICIONÁRIOS
# (Igual a um Array de Structs)
turma = [
    {"id": 1733, "nome": "Carlos", "clube": "Benfica"},  # Índice 0
    {"id": 2050, "nome": "Ana",    "clube": "Porto"},    # Índice 1
    {"id": 3100, "nome": "Pedro",  "clube": "Sporting"}  # Índice 2
]

# 1. Aceder ao Carlos (Índice 0) e ver o Clube
print(f"O aluno {turma[0]['nome']} é do {turma[0]['clube']}")

# 2. Adicionar um novo aluno à lista (com append)
novo_aluno = {"id": 5000, "nome": "Joana", "clube": "Benfica"}
turma.append(novo_aluno)

print(f"\nLista atualizada: {turma}")

# 3. Percorrer a lista toda (Vamos aprender isto melhor a seguir)
print("\n--- Relatório da Turma ---")
for aluno in turma:
    print(f"ID: {aluno['id']} | Nome: {aluno['nome']}")