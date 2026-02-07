import os
os.system('cls' if os.name == 'nt' else 'clear')

class Pessoa:
    
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, o meu nome é {self.nome} ")
        
    def verificar_maioridade(self):
        if self.idade >= 18:
            print(f"O {self.nome} é maior de idade")
        else:
            print(f"O {self.nome} é menor de idade")
            
pessoa1 = Pessoa("Carlos",20)
pessoa1.apresentar()
pessoa1.verificar_maioridade()

pessoa2 = Pessoa("Carol",17)
pessoa2.apresentar()
pessoa2.verificar_maioridade()

