import os
os.system('cls' if os.name == 'nt' else 'clear')

class Secretaria:
    def __init__(self):
        self.alunos = {
            "Carlos": {
                "Idade": 51,
                "Telefone": "911222333",
                "Notas": {"IA": 14, "Python": 16, "Matemática": 10}
            },
            "Carol": {
                "Idade": 31,
                "Telefone": "922333444",
                "Notas": {"IA": 18, "Python": 19, "Matemática": 15}
            },
            "Monica": {
                "Idade": 34,
                "Telefone": "933444555",
                "Notas": {"IA": 16, "Python": 14, "Matemática": 16}
            }
        }

    def ver_ficha_completa(self, nome):
        if nome in self.alunos:
            dados = self.alunos[nome]
            print(f"\n--- Ficha de {nome} ---")
            print(f"Idade: {dados['Idade']}")
            print(f"Contacto: {dados['Telefone']}")
            print("Notas:")
            # Lembra-te do .items() para ver a Cadeira e a Nota! [cite: 94]
            for disc, nota in dados['Notas'].items():
                print(f"  -> {disc}: {nota}")
        else:
            print("Aluno não encontrado!")

# Execução
estgv = Secretaria()
estgv.ver_ficha_completa("Carlos")
estgv.ver_ficha_completa("Carol")
estgv.ver_ficha_completa("Monica")