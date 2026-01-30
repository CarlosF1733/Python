import os
os.system('cls' if os.name == 'nt' else 'clear')

class Telemovel:
    
    def __init__(self, marca):
        self.marca = marca
        self.bateria = 100
        
    def telefonar(self):
        print(f"A ligar de um telemóvel da marca {self.marca}")
        self.bateria -= 10
        
    def estado(self):
        print(f"A bateria do {self.marca} está a {self.bateria}% de carga")
        
        
tel1 = Telemovel("Samsung")     
tel1.estado()
tel1.telefonar()  
tel1.estado()

tel2 = Telemovel("Nokia")     
tel2.estado()  
tel2.telefonar()  
tel1.estado()
    
        