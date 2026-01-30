import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. A nossa lista de notas
notas = [5, 12, 16, 8, 19, 20]

# 2. Definição da Função com Return
def calcular_media_turma(lista_notas, curso="Sistemas Operativos"):
    print(f"--- Processando Notas de {curso} ---")
    
    # Slicing: ignoramos a primeira e a última
    notas_reais = lista_notas[1:-1] 
    
    # Calculamos a média
    media = sum(notas_reais) / len(notas_reais)
    
    # O return devolve o valor para fora da função
    return media

# 3. Chamada da Função e uso do resultado
resultado_media = calcular_media_turma(notas)

print(f"A média final das notas reais é: {resultado_media:.2f}")