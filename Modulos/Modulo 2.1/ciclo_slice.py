# 1. A nossa lista de notas
notas = [5, 12, 16, 8, 19, 20] # O 5 é diagnóstico, o 20 é bónus

# 2. Definição da Função
def avaliar_turma(lista_notas, curso="Sistemas Operativos"):
    print(f"--- Relatório de {curso} ---")
    
    # Slicing: Vamos pegar do segundo elemento até ao penúltimo
    notas_reais = lista_notas[1:-1] 
    
    for n in notas_reais:
        # Lógica Condicional
        if n >= 10:
            status = "Aprovado"
        elif 7 <= n < 10:
            status = "Recurso"
        else:
            status = "Reprovado"
        
        print(f"Nota {n}: {status}")

# 3. Chamada da Função
avaliar_turma(notas)