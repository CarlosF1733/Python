import os
os.system('cls' if os.name == 'nt' else 'clear')

class BaseDados:
    def __init__(self):
        # Dicionário Principal: Chave = Nome do Aluno
        self.bd_escola = {
            "Carlos Fonseca": {
                "Curso": "Eng. Informática (ESTGV)",
                "Telemovel": "961234567",
                "Morada": {"Cidade": "Viseu", "CP": "3500-123"},
                "Notas": {"Python": 18, "Sist. Operativos": 16, "Redes": 15}
            },
            "Carol Martins": {
                "Curso": "Artes Plásticas (ESAP)",
                "Telemovel": "912345678",
                "Morada": {"Cidade": "Lisboa", "CP": "1000-050"},
                "Notas": {"Pintura": 19, "Escultura": 18, "História Arte": 17}
            },
            "Monica Tavares": {
                "Curso": "Biologia (UBM)",
                "Telemovel": "933456789",
                "Morada": {"Cidade": "Aveiro", "CP": "3800-200"},
                "Notas": {"Genética": 14, "Botânica": 15, "Química": 16}
            }
        }

    def relatorio_geral(self):
        print("--- LISTA COMPLETA DE ALUNOS ---")
        
        # 1. Primeiro Loop: Percorre os Alunos (Chave=Nome, Valor=Detalhes)
        for nome, dados in self.bd_escola.items():
            print(f"\nALUNO: {nome}")
            print(f"Curso: {dados['Curso']}")
            print(f"Telemóvel: {dados['Telemovel']}")
            
            # Aceder ao dicionário 'Morada'
            cidade = dados['Morada']['Cidade']
            cp = dados['Morada']['CP']
            print(f"Localidade: {cidade} ({cp})")
            
            print("Pauta:")
            # 2. Segundo Loop: Percorre as notas dentro dos detalhes
            for disciplina, nota in dados['Notas'].items():
                print(f"   -> {disciplina}: {nota} valores")
            
            print("-" * 30)

# Execução
sistema = BaseDados()
sistema.relatorio_geral()