import os

# Limpa o terminal para uma leitura limpa
os.system('cls' if os.name == 'nt' else 'clear')

# --- CLASSE 1: Portáteis ---
class Portatil:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram

    def apresentar(self):
        print(f"[PORTÁTIL] {self.marca} | RAM: {self.ram}GB")

# --- CLASSE 2: Telemóveis ---
class Telemovel:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def apresentar(self):
        print(f"[TELEMÓVEL] {self.marca} {self.modelo}")

# --- CLASSE 3: A Loja Genérica ---
class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.stock = []

    # Repara: 'item' pode ser qualquer objeto que tenha .marca e .apresentar()
    def adicionar_produto(self, item):
        self.stock.append(item)
        print(f"Sucesso: {item.marca} adicionado ao stock da {self.nome}.")

    def mostrar_inventario(self):
        print(f"\n{'='*10} INVENTÁRIO {self.nome} {'='*10}")
        if not self.stock:
            print("Stock vazio.")
        else:
            for produto in self.stock:
                produto.apresentar() # Chama o método de cada classe específica
        print("="*40)

# --- EXECUÇÃO ---

# Criamos a loja
minha_loja = Loja("Global Tech")

# Criamos produtos de tipos diferentes
p1 = Portatil("Asus", 16)
p2 = Portatil("HP", 8)
t1 = Telemovel("Apple", "iPhone 15")
t2 = Telemovel("Samsung", "S24 Ultra")

# Adicionamos tudo usando a MESMA função
minha_loja.adicionar_produto(p1)
minha_loja.adicionar_produto(t1)
minha_loja.adicionar_produto(p2)
minha_loja.adicionar_produto(t2)

# Mostramos o resultado
minha_loja.mostrar_inventario()