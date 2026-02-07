import os
os.system('cls' if os.name == 'nt' else 'clear')

def nome_da_funcao(parametro1, parametro2):
    soma = parametro1 + parametro2
    return soma


resultado = nome_da_funcao(10,20)

print(f"Soma: {resultado}")