import os
os.system('cls' if os.name == 'nt' else 'clear')

aluno_escolhido = "1733"  # Podes mudar para o número que quiseres
with open('Ficheiros/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

# print(f"O aluno {aluno_escolhido} existe!" if f"aluno: {aluno_escolhido}" in conteudo else "Não encontrado.")

if f"aluno: {aluno_escolhido}" in conteudo:
    print(f"O aluno {aluno_escolhido} existe!")
else: 
    print(f"O aluno {aluno_escolhido} não existe!")