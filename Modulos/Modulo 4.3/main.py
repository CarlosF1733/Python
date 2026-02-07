import os
# Importamos a Loja do database e as Classes do models
from database import Loja
from models import Telemovel, Portatil

if __name__ == "__main__":
    minha_loja = Loja() # Ele sabe onde está o ficheiro json através do database.py

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== GESTÃO DE STOCK (Modular) ===")
        print("1. Adicionar Telemóvel")
        print("2. Adicionar Portátil")
        print("3. Ver Stock")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            try:
                print("\n-- Novo Telemóvel --")
                m = input("Marca: ")
                mod = input("Modelo: ")
                p = float(input("Preço: "))
                c = int(input("Câmara (MP): "))
                # Cria objeto usando a classe importada de models.py
                t = Telemovel(m, mod, p, c)
                minha_loja.adicionar(t)
                input("\n>> Telemóvel gravado! Enter para continuar...")
            except ValueError:
                input("\n>> Erro: Valores inválidos!")

        elif opcao == "2":
            try:
                print("\n-- Novo Portátil --")
                m = input("Marca: ")
                mod = input("Modelo: ")
                p = float(input("Preço: "))
                r = int(input("RAM (GB): "))
                pc = Portatil(m, mod, p, r)
                minha_loja.adicionar(pc)
                input("\n>> Portátil gravado! Enter para continuar...")
            except ValueError:
                input("\n>> Erro: Valores inválidos!")

        elif opcao == "3":
            minha_loja.listar()
            input("\n>> Pressione Enter para voltar ao menu...")

        elif opcao == "0":
            print("A sair...")
            break