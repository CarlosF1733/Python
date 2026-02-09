import os
os.system('cls' if os.name == 'nt' else 'clear')

# --- DEFINIÇÃO DA CLASSE ---
class Camiao:
    def __init__(self, modelo, combustivel):
        self.modelo = modelo
        self.combustivel = combustivel

    def viagem(self, kms):
        gasto = kms * 2
        if self.combustivel >= gasto:
            self.combustivel -= gasto
            return True  # Sucesso!
        return False     # Sem combustível suficiente

# --- PREPARAÇÃO DOS DADOS ---
c1 = Camiao("Volvo FH", 100)
c2 = Camiao("Scania R500", 60)
c3 = Camiao("Mercedes Actros", 140)

frota = [c1, c2, c3]

# Criar a pasta se não existir (Dica de "Pro" que te dei)
os.makedirs("Treino", exist_ok=True)

# --- EXECUÇÃO E REGISTO EM FICHEIRO ---
print("Iniciando a logística da frota...")

# Abrimos o ficheiro UMA VEZ e mantemos aberto durante todo o ciclo
with open("Treino/log_frota.txt", "w", encoding="utf-8") as ficheiro:
    ficheiro.write("DIÁRIO DE BORDO DA FROTA\n")
    ficheiro.write("=" * 30 + "\n")

    # Enquanto houver pelo menos um camião que consiga fazer 10km (gasto 20L)
    while any(c.combustivel >= 20 for c in frota):
        for c in frota:
            # Tentamos fazer uma viagem de 10km
            if c.viagem(10):
                msg = f"O {c.modelo} percorreu 10km. Restam {c.combustivel}L no depósito.\n"
                print(msg.strip()) # Mostra no ecrã
                ficheiro.write(msg) # Escreve no ficheiro
            else:
                # Opcional: avisar que este camião parou
                if c.combustivel > -1: # Para não repetir a mensagem infinitamente
                    print(f"--- {c.modelo} imobilizado (combustível insuficiente) ---")
                    c.combustivel = -1 # Marcador para sabermos que já avisámos

    ficheiro.write("\n" + "=" * 30 + "\n")
    ficheiro.write("FIM DA OPERAÇÃO - TODOS OS VEÍCULOS PARADOS")

print("\nOperação concluída! Abre o ficheiro 'Treino/log_frota.txt' para ver o log.")