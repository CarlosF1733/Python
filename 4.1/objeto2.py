import os
os.system('cls' if os.name == 'nt' else 'clear')

class Portatil:
    # O que eu tenho (dados)
    
    def __init__(self, marca, ram):
        self.marca = marca   # grava a marca dentro deste objeto
        self.ram = ram # grava o modelo dentro deste objeto
        
     # O que eu faço (ações / metodos)
     # NOTA: todas as funções da classe precisam do (self)
    def apresentar(self):
         print(f"Olá, sou um {self.marca} com {self.ram} de RAM.")
         
    def upgrade_ram(self, extra):
        self.ram += extra
        print(f"Upgrade feito! Agora tenho {self.ram}GB")
    
# --- Fim da Classe (agora vamos usar) ---
meu_pc = Portatil("Asus", 16)

# Agora mandamos o objeto agir
meu_pc.apresentar() # Ele faz o print sozinho
meu_pc.upgrade_ram(16) # Ele soma a RAM sozinho