import os
# Limpa o terminal (no Windows usa 'cls')
os.system('cls')

variavel = 1733        # int
print(f"Tipo inicial: {type(variavel)}")

variavel = "Benfica"   # Agora é str (string)
print(f"Tipo atual: {type(variavel)}")

# Slicing de String (algo que em C exigiria um ciclo ou memcpy)
print(f"As primeiras 3 letras: {variavel[:3]}")

clube = "Benfica"

# O que será que isto imprime?
print(f"Resultado 1: {clube[0:3]}")
print(f"Resultado 2: {clube[3:]}")
print(f"Resultado 3: {clube[-1]}")