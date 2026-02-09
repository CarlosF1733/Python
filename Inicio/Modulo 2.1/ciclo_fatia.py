import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. Criar a lista mista [Nota, ID_Aluno]
# Vamos imaginar as notas do teu grupo de estudo
registo_escolar = [16, "AL01", 8, "AL02", 12, "AL03", 19, "AL04", 7, "AL05"]

def processar_pauta(lista):
    # 2. Slicing com Step para separar os dados
    # Começa no 0, vai até ao fim, salta de 2 em 2 (Notas)
    notas = lista[::2]
    
    # Começa no 1, vai até ao fim, salta de 2 em 2 (IDs)
    ids = lista[1::2]
    
    print("--- ANÁLISE DE RESULTADOS ---")
    
    # 3. Usar max() e min() nas notas extraídas
    melhor_nota = max(notas)
    pior_nota = min(notas)
    
    # 4. Descobrir quem teve essas notas usando o .index()
    # O índice da nota na lista 'notas' é o mesmo que o do aluno na lista 'ids'
    aluno_topo = ids[notas.index(melhor_nota)]
    aluno_base = ids[notas.index(pior_nota)]
    
    print(f"Melhor Aluno: {aluno_topo} com {melhor_nota} valores.")
    print(f"Aluno em Risco: {aluno_base} com {pior_nota} valores.")
    print("-" * 30)
    
    # 5. Listar tudo usando um for
    print("Pauta Completa:")
    for i in range(len(notas)):
        print(f"ID: {ids[i]} | Nota: {notas[i]}")

# Chamada da função
processar_pauta(registo_escolar)