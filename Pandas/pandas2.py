import os
import pandas as pd

# A tua linha de limpeza (estilo 'nt' vs 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

# Configuração para mostrar 2 casas decimais no terminal
pd.options.display.float_format = '{:.2f}'.format

# --- A MUDANÇA ESTÁ AQUI ---
# Em vez de um dicionário, lemos o ficheiro que criaste
df = pd.read_csv('Pandas/dados.csv')

# 2. Cálculo da coluna Total (Igual ao anterior)
df["Total_Venda"] = df["Quantidade"] * df["Preco_Unit"]

# --- ESTATÍSTICAS INDIVIDUAIS ---
soma_total      = df["Total_Venda"].sum()
media_precos    = df["Preco_Unit"].mean()
venda_maxima    = df["Total_Venda"].max()
venda_minima    = df["Total_Venda"].min()
contagem_itens  = df["Total_Venda"].count()
mediana_vendas  = df["Total_Venda"].median()
desvio_padrao   = df["Total_Venda"].std()
variancia       = df["Total_Venda"].var()
q1_vendas       = df["Total_Venda"].quantile(0.25)
q2_vendas       = df["Total_Venda"].quantile(0.50)
q3_vendas       = df["Total_Venda"].quantile(0.75)

# --- OUTPUT ---
print("-" * 60)
print("RELATÓRIO A PARTIR DE CSV - MODO DATA SCIENCE")
print("-" * 60)
print(df)
print("\n")
print("-" * 60)
print("ESTATÍSTICAS DETALHADAS")
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
print(f"3º Quartil (75%):    {q3_vendas:.2f} €\n")
print("-" * 60)

print("COMPARAÇÃO COM O COMANDO DESCRIBE()")
print("-" * 60)
print(df.describe())
print("-" * 60)