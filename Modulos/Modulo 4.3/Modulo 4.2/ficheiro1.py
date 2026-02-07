import json
import os

# --- 1. Classes de Modelo (Dados) ---

class Equipamento:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def apresentar(self):
        return f"{self.marca} {self.modelo} | {self.preco:.2f}€"

    # Serialização: Transforma o objeto num dicionário simples
    def to_dict(self):
        return {
            "tipo": "generico",
            "marca": self.marca,
            "modelo": self.modelo,
            "preco": self.preco
        }

class Telemovel(Equipamento):
    def __init__(self, marca, modelo, preco, camara):
        super().__init__(marca, modelo, preco)
        self.camara = camara

    def apresentar(self):
        return super().apresentar() + f" | Cam: {self.camara}MP"

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "telemovel"
        data["camara"] = self.camara
        return data

class Portatil(Equipamento):
    def __init__(self, marca, modelo, preco, ram):
        super().__init__(marca, modelo, preco)
        self.ram = ram

    def apresentar(self):
        return super().apresentar() + f" | RAM: {self.ram}GB"

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "portatil"
        data["ram"] = self.ram
        return data

# --- 2. Classe de Gestão (Loja) ---

class Loja:
    def __init__(self, nome_ficheiro="stock.json"):
        self.stock = []
        
        # --- CAMINHO CORRETO DO FICHEIRO ---
        # Garante que o JSON fica na pasta 4.2 (junto ao script)
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.ficheiro_db = os.path.join(pasta_atual, nome_ficheiro)

        self.carregar_dados()

    def adicionar(self, equipamento):
        self.stock.append(equipamento)
        self.guardar_dados() 

    def listar(self):
        print(f"\n--- Stock ({len(self.stock)} itens) ---")
        for item in self.stock:
            print(item.apresentar())
        print("--------------------------------")

    def guardar_dados(self):
        lista_para_json = [item.to_dict() for item in self.stock]
        
        try:
            with open(self.ficheiro_db, 'w', encoding='utf-8') as f:
                json.dump(lista_para_json, f, indent=4, ensure_ascii=False)
            print(">> Dados guardados em disco.")
        except Exception as e:
            print(f"Erro ao guardar: {e}")

    # AQUI ESTAVA O ERRO (Corrigido)
    def carregar_dados(self):
        if not os.path.exists(self.ficheiro_db):
            return 

        try:
            with open(self.ficheiro_db, 'r', encoding='utf-8') as f:
                lista_lida = json.load(f)
            
            self.stock = []
            
            for d in lista_lida:
                if d["tipo"] == "telemovel":
                    obj = Telemovel(d["marca"], d["modelo"], d["preco"], d["camara"])
                elif d["tipo"] == "portatil":
                    obj = Portatil(d["marca"], d["modelo"], d["preco"], d["ram"])
                else:
                    obj = Equipamento(d["marca"], d["modelo"], d["preco"])
                
                # Esta linha tem de estar DENTRO do for
                self.stock.append(obj)
            
            print(f">> Sistema iniciou com {len(self.stock)} produtos carregados.")
            
        except Exception as e:
            # O except tem de estar alinhado com o try
            print(f"Erro ao ler ficheiro: {e}")
            self.stock = []

# --- 3. Execução ---
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    minha_loja = Loja()

    # Só cria dados de teste se a lista estiver vazia
    if len(minha_loja.stock) == 0:
        print("Stock vazio. A criar dados iniciais...")
        minha_loja.adicionar(Telemovel("Samsung", "S24 Ultra", 1400, 200))
        minha_loja.adicionar(Portatil("Asus", "Zephyrus", 2000, 32))
    
    minha_loja.listar()