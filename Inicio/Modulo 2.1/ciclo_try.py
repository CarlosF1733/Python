import os
os.system('cls' if os.name == 'nt' else 'clear')

try:
    # O Python TENTA executar este bloco
    nota = int(input("Digite a nota do aluno: "))
    
    if 20 >= nota >= 10:
        print("Aprovado!")
    else:
        print("Reprovado!")

except ValueError:
    # Se houver um erro de VALOR, ele salta para aqui em vez de crashar
    print("ERRO: Inseriste texto ou um formato inválido. Usa números (ex: 12.5).")

print("\nO programa continua a correr normalmente...")