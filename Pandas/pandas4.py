import os
import pandas as pd

# A tua linha de limpeza preferida
os.system('cls' if os.name == 'nt' else 'clear')

# Configuração para 2 casas decimais
pd.options.display.float_format = '{:.2f}'.format

# 1. LER DE JSON
# Se tivesses um ficheiro 'dados.json' na pasta Pandas:
# df = pd.read_json('Pandas/dados.csv')

# Usando os nossos dados de exemplo
dados = {
    "Produto": ["Laptop", "Rato", "Monitor", "Teclado", "Webcam"],
    "Quantidade": [2, 15, 5, 10, 4],
    "Preco_Unit": [850.00, 25.90, 160.00, 45.00, 59.90]
}
df = pd.DataFrame(dados)

# 2. CÁLCULOS
df["Total_Venda"] = df["Quantidade"] * df["Preco_Unit"]

# --- OUTPUT NO TERMINAL ---
print("-" * 60)
print("ANÁLISE DE DADOS JSON")
print("-" * 60)
print(df.describe())
print("-" * 60)

# 3. GUARDAR EM JSON
# O argumento 'indent=4' serve para o ficheiro ficar legível para humanos
df.to_json('Pandas/Relatorio_Final.json', orient='records', indent=4)

print("\n✅ Sucesso! O ficheiro 'Relatorio_Final.json' foi criado.")