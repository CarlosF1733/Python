import os
os.system('cls' if os.name == 'nt' else 'clear')

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Notas:
    def __init__(self, numero, n_so, n_rc, n_es):
        self.numero = numero
        self.so = n_so   # Sistemas Operativos
        self.rc = n_rc   # Redes de Computadores
        self.es = n_es   # Engenharia de Software

    def exibir_boletim(self):
        print(f"aluno: {self.numero}")
        print(f"Sistemas Operativos: {self.so}")
        print(f"Redes Computadores: {self.rc}")
        print(f"Engenharia de Software: {self.es}")
        print("-" * 25) # Separador visual

# Criar os 5 alunos (Instâncias)
a1 = Notas(1733, 16, 15, 17)
a2 = Notas(1734, 12, 10, 11)
a3 = Notas(1735, 18, 19, 18)
a4 = Notas(1736, 10, 10, 10)
a5 = Notas(1737, 14, 13, 16)

# Lista com todos
pauta = [a1, a2, a3, a4, a5]

# Print de todos
for aluno in pauta:
    aluno.exibir_boletim()