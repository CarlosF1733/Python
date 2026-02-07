import os

def limpar_terminal():
    # Este código está "dentro" da função (4 espaços de recuo)
    os.system('cls' if os.name == 'nt' else 'clear')

# Este código está "fora" (colado à margem), por isso corre logo
limpar_terminal()

print("O terminal foi limpo com sucesso.")