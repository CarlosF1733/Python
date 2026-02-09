# Ficheiro apenas para definir COMO são os objetos

class Equipamento:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def apresentar(self):
        return f"{self.marca} {self.modelo} | {self.preco:.2f}€"

    def to_dict(self):
        return {
            "tipo": "generico",
            "marca": self.marca,
            "modelo": self.modelo,
            "preco": self.preco
        }

class Telemovel(Equipamento):
    def __init__(self, marca, modelo, preco, camara):
        super().__init__(marca, modelo, preco)
        self.camara = camara

    def apresentar(self):
        return super().apresentar() + f" | Cam: {self.camara}MP"

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "telemovel"
        data["camara"] = self.camara
        return data

class Portatil(Equipamento):
    def __init__(self, marca, modelo, preco, ram):
        super().__init__(marca, modelo, preco)
        self.ram = ram

    def apresentar(self):
        return super().apresentar() + f" | RAM: {self.ram}GB"

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "portatil"
        data["ram"] = self.ram
        return data