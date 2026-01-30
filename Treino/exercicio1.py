import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cao:
    # O "setup" inicial. Corre sempre que crias um cão novo.
    def __init__(self, nome, raca):
        self.nome = nome  # Guarda o nome dentro deste cão específico
        self.raca = raca  # Guarda a raça dentro deste cão específico

    # Uma ação que o cão sabe fazer
    def ladrar(self):
        print(f"O {self.nome} diz: Au au!")
    
    # Para usar a raça 
    def descrever(self):
        print(f"O {self.nome} é um {self.raca}.")
        

# 1. Criar dois cães diferentes (instanciar objetos)
cao1 = Cao("Bobby", "Rafeiro")
cao2 = Cao("Rex", "Pastor Alemão")

# 2. Mete-os a ladrar (chamar o método)
cao1.ladrar()
cao2.ladrar()
cao1.descrever()
cao2.descrever()
        
        