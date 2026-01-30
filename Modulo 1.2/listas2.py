import os

# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_terminal()

# 1. CRIAR
marcas = ["Samsung", "Asus", "Apple"]
print(f"1. Inicial: {marcas}")

# 2. APPEND (Adiciona ao fim)
marcas.append("Dell")
print(f"2. Após Append (Dell): {marcas}")

# 3. INSERT (Coloca no índice 1 e empurra os outros)
marcas.insert(1, "Lenovo")
print(f"3. Após Insert (Lenovo no índice 1): {marcas}")

# 4. REPLACE (Substitui o valor no índice 0 - O Samsung morre aqui)
marcas[0] = "HP"
print(f"4. Após Substituir índice 0 por HP: {marcas}")

# 5. SORT (Ordena A-Z)
marcas.sort()
print(f"5. Após Sort (A-Z): {marcas}")

# 6. REVERSE (Inverte a ordem)
marcas.reverse()
print(f"6. Após Reverse: {marcas}")

# 7. REMOVE (Remove por nome com verificação de segurança)
if "Asus" in marcas:
    marcas.remove("Asus")
    print(f"7. Após Remove Asus: {marcas}")
else:
    print("7. Aviso: A palavra 'Asus' não foi encontrada.")

# 8. POP (Remove por índice e guarda o valor)
if len(marcas) > 0:
    foi_embora = marcas.pop(0)
    print(f"8. Após Pop(0): {marcas} (Saiu o: {foi_embora})\n")