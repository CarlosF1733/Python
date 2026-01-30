import os
os.system('cls' if os.name == 'nt' else 'clear')

# Criar uma lista de marcas de carros
carros = ["Asus", "VivoBook", "Samsung", "S9 FE"] # Usei exemplos dos teus dispositivos
print(f"A minha lista: {carros}")

print(f"\nO primeiro item é: {carros[0]}")
print(f"O último item é: {carros[-1]}\n")

# Ver o tamanho da lista (quantos itens tem)
tamanho = len(carros)
print(f"A lista tem {tamanho} itens.\n")

carros.append("iPhone") # Vamos adicionar um intruso
print(f"Lista após append: {carros}\n")

# Remover pelo nome
carros.remove("Asus") 

# Remover o último e guardar numa variável
ultimo = carros.pop() 

print(f"Lista final: {carros}")
print(f"O item removido com pop foi: {ultimo}\n")

# Se a lista tem 2 itens, o índice 0 é o primeiro e o 1 é o segundo.
# Vamos remover o que estiver na posição 1.
removido_pos1 = carros.pop(1)

print(f"Removi o elemento do meio: {removido_pos1}")
print(f"Lista agora: {carros}\n")