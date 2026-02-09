import os

# Limpa o terminal logo no início
os.system('cls' if os.name == 'nt' else 'clear')

# --- CLASSE 1: O MOLDE DO PRODUTO ---
class Portatil:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram

    def apresentar(self):
        print(f"-> Portátil {self.marca} com {self.ram}GB de RAM.")

    def upgrade_ram(self, extra):
        self.ram += extra
        print(f"[UPGRADE] {self.marca} agora tem {self.ram}GB.")


# --- CLASSE 2: A GESTORA (INTERAÇÃO) ---
class Loja:
    def __init__(self, nome_da_loja):
        self.nome = nome_da_loja
        self.stock = [] # Lista que guardará os OBJETOS da classe Portatil

    def adicionar_ao_stock(self, computador):
        self.stock.append(computador)
        print(f"Sucesso: {computador.marca} guardado na loja {self.nome}.")

    def mostrar_tudo(self):
        print(f"\n=== LISTA DE STOCK: {self.nome} ===")
        if not self.stock:
            print("A loja está vazia.")
        else:
            for item in self.stock:
                # Aqui a Loja usa o método que pertence ao Portatil
                item.apresentar() 
        print("=" * 30)


# --- EXECUTANDO O PROGRAMA ---

# 1. Criamos a loja
minha_loja = Loja("Tech Carlos 2026")

# 2. Criamos alguns objetos Portatil
pc1 = Portatil("Asus", 16)
pc2 = Portatil("MacBook", 8)
pc3 = Portatil("Lenovo", 32)

# 3. Fazemos um upgrade num deles antes de vender
pc2.upgrade_ram(8) 

print("-" * 30)

# 4. Adicionamos os objetos à nossa loja
minha_loja.adicionar_ao_stock(pc1)
minha_loja.adicionar_ao_stock(pc2)
minha_loja.adicionar_ao_stock(pc3)

# 5. Vemos o resultado final
minha_loja.mostrar_tudo()