import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. A ferramenta (Função com "pneu sobresselente")
def conversor(dolar, taxa=1.10):
    return dolar * taxa

# 2. Pedir o valor base
valor = float(input("Quantos dólares tens? "))

# 3. A Lógica de decisão (Tu é que controlas isto)
opcao = input("Queres definir uma taxa personalizada? (s/n): ")

if opcao == 's':
    # Se ele diz SIM, pedimos a taxa nova
    nova_taxa = float(input("Qual é a taxa de conversão? "))
    resultado = conversor(valor, nova_taxa) # Chamamos com 2 argumentos
    print(f"Usada taxa personalizada ({nova_taxa}).")
else:
    # Se ele diz NÃO (ou qualquer outra coisa), usamos o default
    resultado = conversor(valor) # Chamamos só com 1 argumento (o Python usa 1.10)
    print("Usada taxa padrão (1.10).")

print(f"Resultado: {resultado:.2f} €")