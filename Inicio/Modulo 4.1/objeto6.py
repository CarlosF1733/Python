import os

# 1. Classe Mãe (Super Classe)
# Guarda o que é comum a todos os equipamentos para não repetires código.
class Equipamento:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def apresentar(self):
        # O ":.2f" formata o preço para 2 casas decimais
        return f"Equipamento: {self.marca} {self.modelo} | {self.preco:.2f}€"

# 2. Classes Filhas (Subclasses)
# Herdam de Equipamento e só adicionam o que é específico delas.
class Telemovel(Equipamento):
    def __init__(self, marca, modelo, preco, camara):
        super().__init__(marca, modelo, preco)  # Envia dados para a classe mãe
        self.camara = camara

    # Polimorfismo: Reescreve o método apresentar para adicionar detalhes
    def apresentar(self):
        base = super().apresentar()
        return f"{base} | Câmara: {self.camara}MP"

class Portatil(Equipamento):
    def __init__(self, marca, modelo, preco, ram, grafica):
        super().__init__(marca, modelo, preco)
        self.ram = ram
        self.grafica = grafica

    def apresentar(self):
        base = super().apresentar()
        return f"{base} | RAM: {self.ram}GB | GPU: {self.grafica}"

# 3. Gestão
class Loja:
    def __init__(self):
        self.stock = []

    def adicionar_equipamento(self, equipamento):
        self.stock.append(equipamento)
        print("Produto adicionado com sucesso!")

    def listar_stock(self):
        print("\n--- Stock Atual ---")
        for i, item in enumerate(self.stock, 1):
            print(f"{i}. {item.apresentar()}")
        print("-------------------")

# 4. Execução (Menu simples para teste)
minha_loja = Loja()
os.system('cls' if os.name == 'nt' else 'clear')

# Adicionando objetos manualmente para testar a herança
t1 = Telemovel("Samsung", "A26", 300, 50)
p1 = Portatil("Asus", "VivoBook", 900, 16, "2GB Dedicados")

minha_loja.adicionar_equipamento(t1)
minha_loja.adicionar_equipamento(p1)

minha_loja.listar_stock()