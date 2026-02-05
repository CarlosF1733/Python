import os
import pandas as pd

# A tua linha de limpeza (estilo 'nt' vs 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

# Configuração para mostrar 2 casas decimais no terminal
pd.options.display.float_format = '{:.2f}'.format

# 1. LER DO EXCEL
# Se o teu ficheiro se chamar 'vendas.xlsx' e estiver na pasta Pandas:
# df = pd.read_excel('Pandas/vendas.xlsx')

# Para este teste, vamos usar os dados que já temos
dados = {
    "Produto": ["Laptop", "Rato", "Monitor", "Teclado", "Webcam"],
    "Quantidade": [2, 15, 5, 10, 4],
    "Preco_Unit": [850.00, 25.90, 160.00, 45.00, 59.90]
}
df = pd.DataFrame(dados)

# 2. CÁLCULOS (Modo Data Science)
df["Total_Venda"] = df["Quantidade"] * df["Preco_Unit"]

# --- OUTPUT NO TERMINAL ---
print("-" * 60)
print("ANÁLISE DE DADOS EXCEL")
print("-" * 60)
print(df.describe())
print("-" * 60)

# 3. GUARDAR NUM NOVO FICHEIRO EXCEL
# Este comando cria um ficheiro .xlsx real que podes abrir no Excel/Sheets
df.to_excel('Pandas/Relatorio_Final.xlsx', index=False)

print("\n✅ Sucesso! O ficheiro 'Relatorio_Final.xlsx' foi criado na pasta Pandas.")