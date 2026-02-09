import os
os.system('cls' if os.name == 'nt' else 'clear')

pauta = {"AL01": 16, "AL02": 8}

# SEM .items() -> Só recebes a chave
print("Só chaves:")
for x in pauta:
    print(x) # Imprime: AL01, AL02

# COM .items() -> Recebes os dois (precisas de duas variáveis no for)
print("\nPar completo:")

# O .items() serve para ele te entregar o par completo (Chave e Valor)
# Este comando for, atribui à variavel aluno a chave e á variavel nota o valor, até acbar a lista em ciclo
for aluno, nota in pauta.items(): 
    print(f"O {aluno} teve {nota}")