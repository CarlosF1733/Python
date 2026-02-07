import json
import os
# IMPORTANTE: Estamos a ir buscar as classes ao outro ficheiro
from models import Equipamento, Telemovel, Portatil 

class Loja:
    def __init__(self, nome_ficheiro="stock.json"):
        self.stock = []
        
        # Caminho relativo a ESTE ficheiro database.py
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.ficheiro_db = os.path.join(pasta_atual, nome_ficheiro)

        self.carregar_dados()

    def adicionar(self, equipamento):
        self.stock.append(equipamento)
        self.guardar_dados() 

    def listar(self):
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