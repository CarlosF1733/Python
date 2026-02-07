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

a1 = Atleta("Carlos", 90)
a2 = Atleta("Carol", 80)
a3 = Atleta("Monica", 70)
equipa = [a1, a2, a3]

# 1. Primeiro: O treino acontece (o while)
while any(atleta.energia > 0 for atleta in equipa): 
    for atleta in equipa:
        atleta.treinar()

# 2. Segundo: Gravas os resultados finais no ficheiro
with open("Treino/relatorio.txt", "w") as ficheiro:
    ficheiro.write("RELATÓRIO DE TREINO FINAL\n")
    ficheiro.write("-------------------\n")
    for atleta in equipa:
        # Aqui gravamos o estado final de cada um
        ficheiro.write(f"Atleta: {atleta.nome} | Energia Final: {atleta.energia}\n")

print("Verifica o ficheiro 'relatorio.txt'.")