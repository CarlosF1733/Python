import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. CRIAR um Dicionário (Usa chavetas { } )
# Ao contrário das listas, aqui damos nomes aos campos (Chave: Valor)
meu_perfil = {
    "nome": "Carlos",
    "clube": "Benfica",
    "ano_nascimento": 1974,
    "cidade": "Viseu",
    "estudante": True
}

print(f"1. Perfil inicial: {meu_perfil}\n")

# 2. ACEDER (Lê-se pela 'etiqueta', não por 0, 1 ou 2)
print(f"2. O meu nome é: {meu_perfil['nome']}")
print(f"3. O meu clube é: {meu_perfil['clube']}")

# 3. ADICIONAR (Basta inventar uma etiqueta nova e dar-lhe valor)
meu_perfil["telemovel"] = "Samsung"
print(f"\n4. Após adicionar telemóvel: {meu_perfil}")

# 4. ALTERAR (Usa-se a mesma etiqueta com valor novo)
meu_perfil["clube"] = "Benfica Glorioso"
print(f"5. Após alterar o clube: {meu_perfil['clube']}")

# 5. REMOVER (Usa-se a etiqueta)
del meu_perfil["estudante"]
print(f"\n6. Após apagar estudante: {meu_perfil}")