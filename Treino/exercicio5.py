import os
os.system('cls' if os.name == 'nt' else 'clear')

class Atleta:
    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        
    def treinar(self):
        if self.energia > 0:
            self.energia -= 10
            print(f"O {self.nome} treinou!! Energia atual: {self.energia}")
        else:
            print(f"O {self.nome} está exausto e não pode treinar!")
        
a1 = Atleta("Carlos",90)
a2 = Atleta("Carol",80)
a3 = Atleta("Monica", 70)

equipa = [a1,a2,a3]

# enquanto na lista equipa = [("Carlos",90) ; ("Carol",80) ; ("Monica", 70) ]
# ele sabe que a lista tem = [(nome1, energia1) ; (nome2, energia2) ; (nome3 , energia3)]
# e nós só queremos a energia do atleta na lista logo fica resumida a [90;80;70]
#sempre que correr o while vai decrementar todos 10 até termos [0 ; 0 ;0] só assim pára
while any(atleta.energia > 0 for atleta in equipa): 
    for atleta in equipa:
        atleta.treinar()  