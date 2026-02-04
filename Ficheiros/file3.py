import os
# Comando para limpar o terminal conforme as tuas instruções guardadas
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
        print("-" * 25)

# Criar os 5 alunos (Instâncias)
a1 = Notas(1733, 16, 15, 17)
a2 = Notas(1734, 12, 10, 11)
a3 = Notas(1735, 18, 19, 18)
a4 = Notas(1736, 10, 10, 10)
a5 = Notas(1737, 14, 13, 16)

# Lista com todos
pauta = [a1, a2, a3, a4, a5]

# Print de todos no terminal
for aluno in pauta:
    aluno.exibir_boletim()

# --- PARTE DE GRAVAÇÃO COM VERIFICAÇÃO ---

caminho = 'Ficheiros/registos.txt'

# 1. Garantir que a pasta existe (apenas por segurança)
if not os.path.exists('Ficheiros'):
    os.makedirs('Ficheiros')

# 2. LER o que já lá está para evitar duplicados [cite: 138, 139]
# Partimos do princípio que o ficheiro existe conforme pediste
with open(caminho, 'r', encoding='utf-8') as f:
    conteudo_atual = f.read()

# 3. ABRIR em modo append ('a') para acrescentar apenas novos [cite: 175]
with open(caminho, 'a', encoding='utf-8') as f:
    for aluno in pauta:
        termo_busca = f"aluno: {aluno.numero}"
        
        # Verificamos se o "aluno: XXXX" já existe no texto lido
        if termo_busca in conteudo_atual:
            print(f"O aluno {aluno.numero} já existe no ficheiro. Ignorado.")
        else:
            f.write(f"{termo_busca}\n")
            f.write(f"Sistemas Operativos: {aluno.so}\n")
            f.write(f"Redes Computadores: {aluno.rc}\n")
            f.write(f"Engenharia de Software: {aluno.es}\n")
            f.write("-" * 25 + "\n")
            print(f"Aluno {aluno.numero} gravado com sucesso!")

print(f"\nProcesso concluído em '{caminho}'.")