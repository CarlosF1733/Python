import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Criar uma tabela simples de teste
dados = {'Alunos': ['Eu', 'Tu'], 'Nota': [20, 18]}
df = pd.DataFrame(dados)

print("--- O PANDAS ESTÁ A FUNCIONAR ---")
print(df)