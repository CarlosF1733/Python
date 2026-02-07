import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ler o ficheiro (se guardaste como Excel, usa pd.read_excel)
df = pd.read_csv('Pandas/notas.csv') 

print("--- DADOS LIDOS DO FICHEIRO ---")
print(df)