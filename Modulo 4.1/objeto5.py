import os

# Limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')

class Portatil:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram

    def apresentar(self):
        print(f"[PORTÁTIL] {self.marca} | RAM: {self.ram}GB")

class Telemovel:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def apresentar(self):
        print(f"[TELEMÓVEL] {self.marca} {self.modelo}")

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.stock = []

    def adicionar_produto(self, item):
        self.stock.append(item)
        print(f"Sucesso: {item.marca} guardado na {self.nome}.")

    def mostrar_inventario(self):
        print(f"\n=== INVENTÁRIO {self.nome} ===")
        for produto in self.stock:
            produto.apresentar()
        print("="*30)

# --- EXECUÇÃO ---
minha_loja = Loja("Global Tech")

# Adicionamos algo automático só para a lista não estar vazia
minha_loja.adicionar_produto(Portatil("Asus", 16))

# --- PARTE NOVA: INTERAÇÃO COM O UTILIZADOR ---

print("\n--- Adicionar Novo Telemóvel ---")
marca_user = input("Digite a marca do telemóvel: ")
modelo_user = input("Digite o modelo do telemóvel: ")

# Criamos o objeto com o que o utilizador escreveu
novo_telt = Telemovel(marca_user, modelo_user)
minha_loja.adicionar_produto(novo_telt)

# Mostramos como ficou o stock
minha_loja.mostrar_inventario()

# Linha final para o programa não fechar de imediato em alguns sistemas
input("\nPressione Enter para sair...")