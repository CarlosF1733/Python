import os
import pandas as pd

# A tua linha de limpeza (estilo 'nt' vs 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

# Configura o Pandas para mostrar 2 casas decimais em tudo
pd.options.display.float_format = '{:.2f}'.format

# 1. Os dados
dados = {
    "Produto": ["Laptop", "Rato", "Monitor", "Teclado", "Webcam"],
    "Quantidade": [2, 15, 5, 10, 4],
    "Preco_Unit": [850.00, 25.90, 160.00, 45.00, 59.90]
}

df = pd.DataFrame(dados)

# 2. Cálculo da coluna Total (Operação Vetorial)
df["Total_Venda"] = df["Quantidade"] * df["Preco_Unit"]

# --- TODAS AS OPÇÕES SEGUIDAS (Arsenal Completo Fase 1) ---

soma_total      = df["Total_Venda"].sum()
media_precos    = df["Preco_Unit"].mean()
venda_maxima    = df["Total_Venda"].max()
venda_minima    = df["Total_Venda"].min()
contagem_itens  = df["Total_Venda"].count()
mediana_vendas  = df["Total_Venda"].median()
desvio_padrao   = df["Total_Venda"].std()
variancia       = df["Total_Venda"].var()

# Medidas de Posição (Quartis)
q1_vendas       = df["Total_Venda"].quantile(0.25)
q2_vendas       = df["Total_Venda"].quantile(0.50) # Igual à mediana
q3_vendas       = df["Total_Venda"].quantile(0.75)

# --- OUTPUT 1 comandos separados ---
print("-" * 60)
print("RELATÓRIO ESTATÍSTICO COMPLETO - MODO DATA SCIENCE")
print("-" * 60)
print(df)
print("\n")
print("-" * 60)
print("Usando todos os comandos")
print("-" * 60)
print(f"Soma Total:          {soma_total:.2f} €")
print(f"Média de Preços:     {media_precos:.2f} €")
print(f"Venda Máxima:        {venda_maxima:.2f} €")
print(f"Venda Mínima:        {venda_minima:.2f} €")
print(f"Nº de Registos:      {contagem_itens}")
print(f"Mediana (Q2):        {mediana_vendas:.2f} €")
print(f"Desvio Padrão:       {desvio_padrao:.2f}")
print(f"Variância:           {variancia:.2f}")
print(f"1º Quartil (25%):    {q1_vendas:.2f} €")
print(f"2º Quartil (50%):    {q2_vendas:.2f} €")
print(f"3º Quartil (75%):    {q3_vendas:.2f} €\n")
print("-" * 60)

# --- OUTPUT 2: Usando o comando describe() ---

print("COMPARAÇÃO COM O COMANDO DESCRIBE()")
print("-" * 60)
# O describe() analisa todas as colunas numéricas automaticamente
print(df.describe())
print("-" * 60)