import os
os.system('cls' if os.name == 'nt' else 'clear')

class Telemovel:
    # O Construtor (O Setup inicial)
    # self = o telemovel especifico que está a nascer
    # marca, modelo = os dados que vamos passar
    
    def __init__(self, marca, modelo):
        self.marca = marca   # grava a marca dentro deste objeto
        self.modelo = modelo # grava o modelo dentro deste objeto
        
# --- Fim da Classe (agora vamos usar) ---

# Criar o Objeto 1 (O __init__ corre aqui)
tel1 = Telemovel("Samsung","A71")  

# Criar o Objeto 1 (O __init__ corre aqui)
tel2 = Telemovel("Samsung","A26")  

# Aceder aos dados (Notação de ponto)
print(f"O Telemovél 1 é um {tel1.marca} {tel1.modelo}")
print(f"O Telemovél 2 é um {tel2.marca} {tel2.modelo}")