import os
os.system('cls' if os.name == 'nt' else 'clear')

class Produto:

    def __init__(self,nome,stock):
        self.nome = nome
        self.stock = stock
    
    def venda(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            print(f"Produto {self.nome} esgotado!")
  
       
P1 = Produto("Caneta",20)
P2 = Produto("Caderno",17)
P3 = Produto("Borracha",14)

loja = [P1,P2,P3]

while any(produto.stock > 0 for produto in loja):
    for produto in loja:
        produto.venda()
        print(f"Produto: {produto.nome} | Stock: {produto.stock}")
 
print("-" * 20)  
for produto in loja: 
    print(f"Stock Final => Produto: {produto.nome} | Stock: {produto.stock}")    
    
with open("Treino/historico_stock.txt", "a", encoding="utf-8") as ficheiro:
    ficheiro.write("PRODUTOS EM STOCK\n")
    for produto in loja: 
        ficheiro.write(f"Stock Final => Produto: {produto.nome} | Stock: {produto.stock}\n")
        
print("\n--- LENDO O FICHEIRO ---")
with open("Treino/historico_stock.txt", "r", encoding="utf-8") as ficheiro:
    print(f"\n A ler do ficheiro {ficheiro.name}")
    print(ficheiro.read())