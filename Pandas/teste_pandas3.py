import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. Ler o ficheiro (garante que o notas.csv está na pasta certa!)
df = pd.read_csv('Pandas/notas.csv') 

# 2. Criar coluna nova 'Final' (Média aritmética)
# O Pandas soma a coluna inteira 'Teste1' com a 'Teste2' e divide por 2
df['Final'] = (df['Teste1'] + df['Teste2']) / 2

print("--- PAUTA COM MÉDIAS ---")
print(df)