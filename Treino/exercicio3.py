import os
os.system('cls' if os.name == 'nt' else 'clear')

class Carro:
    
    def __init__(self, cor):
        self.cor = cor
        self.combustivel = 100
        print(f"O carro é da cor {self.cor} e tem {self.combustivel} no depósito")
        
    def pintar(self,nova_cor):
        self.cor = nova_cor
        print(f"O carro é da cor {self.cor}")
        
    def conduzir(self):
        self.combustivel -= 20
        print(f"O carro está a andar e tem {self.combustivel} no depósito")
        
    def exibir_estado(self):
        print(f"A cor do carro é {self.cor} e restam {self.combustivel} litros")  
             
    
car1 = Carro("Vermelho")
car1.exibir_estado()
car1.conduzir()
car1.pintar("Preto")
car1.exibir_estado()
    
        
         