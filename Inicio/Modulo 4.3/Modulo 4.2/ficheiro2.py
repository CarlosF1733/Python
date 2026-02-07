import json
import os

# ==========================================
# 1. CLASSES DE MODELO (DADOS)
# ==========================================

class Equipamento:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def apresentar(self):
        return f"{self.marca} {self.modelo} | {self.preco:.2f}€"

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

# ==========================================
# 2. CLASSE DE GESTÃO (LÓGICA + FICHEIROS)
# ==========================================

class Loja:
    def __init__(self, nome_ficheiro="stock.json"):
        self.stock = []
        
        # Garante que o ficheiro fica na mesma pasta do script
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.ficheiro_db = os.path.join(pasta_atual, nome_ficheiro)

        self.carregar_dados()

    def adicionar(self, equipamento):
        self.stock.append(equipamento)
        self.guardar_dados() 

    def listar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n--- STOCK ATUAL ({len(self.stock)} itens) ---")
        for item in self.stock:
            print(item.apresentar())
        print("------------------------------------------")

    def guardar_dados(self):
        lista_para_json = [item.to_dict() for item in self.stock]
        
        try:
            with open(self.ficheiro_db, 'w', encoding='utf-8') as f:
                json.dump(lista_para_json, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao guardar: {e}")

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
                
                self.stock.append(obj)
            
        except Exception as e:
            print(f"Erro ao ler ficheiro: {e}")
            self.stock = []

# ==========================================
# 3. INTERFACE DE UTILIZADOR (MENU)
# ==========================================

if __name__ == "__main__":
    minha_loja = Loja()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== GESTÃO DE STOCK ===")
        print("1. Adicionar Telemóvel")
        print("2. Adicionar Portátil")
        print("3. Ver Stock")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            try:
                print("\n-- Novo Telemóvel --")
                m = input("Marca: ")
                mod = input("Modelo: ")
                p = float(input("Preço: "))
                c = int(input("Câmara (MP): "))
                t = Telemovel(m, mod, p, c)
                minha_loja.adicionar(t)
                input("\n>> Telemóvel gravado! Enter para continuar...")
            except ValueError:
                input("\n>> Erro: Introduza números válidos no preço/câmara!")

        elif opcao == "2":
            try:
                print("\n-- Novo Portátil --")
                m = input("Marca: ")
                mod = input("Modelo: ")
                p = float(input("Preço: "))
                r = int(input("RAM (GB): "))
                pc = Portatil(m, mod, p, r)
                minha_loja.adicionar(pc)
                input("\n>> Portátil gravado! Enter para continuar...")
            except ValueError:
                input("\n>> Erro: Introduza números válidos no preço/RAM!")

        elif opcao == "3":
            minha_loja.listar()
            input("\n>> Pressione Enter para voltar ao menu...")

        elif opcao == "0":
            print("A sair...")
            break
            
        else:
            input("Opção inválida! Enter para tentar de novo...")