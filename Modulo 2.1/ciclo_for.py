import os
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(5):
    print(f"Esta é a volta número {i}")

notas_da_turma = [16, 8, 12, 19, 5]

for n in notas_da_turma:
    if n >= 10:
        print(f"Nota {n}: Aprovado!")
    else:
        print(f"Nota {n}: Reprovado. Estuda mais!") 