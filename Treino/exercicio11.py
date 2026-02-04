import os
os.system('cls' if os.name == 'nt' else 'clear')

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas # Ex: {"IA": 15, "Python": 18, "Redes": 12} [cite: 92]

# 1. Criar a lista de objetos [cite: 173]
turma = [
    Aluno("Carlos", {"IA": 14, "Python": 16, "Matemática": 10}),
    Aluno("Carol", {"IA": 18, "Python": 19, "Matemática": 15}),
    Aluno("Mónica", {"IA": 10, "Python": 11, "Matemática": 19})
]

# 2. Apresentar os dados (Treino de iteração dupla)
print("--- PAUTA DA TURMA ---")
for aluno in turma:
    print(f"\nAluno: {aluno.nome}")
    
    # Usar .values() para ler chave e valor ao mesmo tempo [cite: 94]
    for nota in aluno.notas.values():
        print(f"{nota}") 
    
    # Usar .keys() para ler chave e valor ao mesmo tempo [cite: 94]
    for nota in aluno.notas.keys():
        print(f"{nota}") 
    
    # Usar .items() para ler chave e valor ao mesmo tempo [cite: 94]
    for cadeira, nota in aluno.notas.items():
        print(f"- {cadeira}: {nota}")