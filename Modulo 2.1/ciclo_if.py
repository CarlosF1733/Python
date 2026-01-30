import os
os.system('cls' if os.name == 'nt' else 'clear')

nota = 16  # A tua nota de SO
if nota >= 15:
    print(f"Aprovadissimo com {nota}")
elif  (7 <= nota < 10):
    print(f"Recurso com {nota}")
elif (nota >= 10):
    print(f"Aprovado com {nota}")
else:
    print(f"Reprovado sem direito a recurso com {nota}")
