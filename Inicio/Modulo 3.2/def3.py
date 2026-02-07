import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ao colocar taxa=1.10, tornas esse argumento opcional.
# Se quem chama a função não disser nada, o Python assume 1.10.
def conversor(dolar, taxa=1.10):
    euro = taxa * dolar
    return euro

val = float(input("Valor em Dólares: "))

# CASO 1: Não envio a taxa (usa o default 1.10)
res_padrao = conversor(val)
print(f"Com taxa padrão: {res_padrao:.2f} €")

# CASO 2: Envio a taxa (substitui o 1.10 por 1.20)
res_novo = conversor(val, 1.20) 
print(f"Com taxa 1.20:   {res_novo:.2f} €")