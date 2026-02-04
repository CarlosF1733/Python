import os
os.system('cls' if os.name == 'nt' else 'clear')

class BaseDados:
    def __init__(self):
        self.bd_escola = {
            "aluno_01": {
                "Estudante": {"Nome": "Carlos", "Apelido": "Fonseca"},
                "CC": "12345678", 
                "Idade": 51,
                "Colocacao": {"Curso": "Eng. Informática", "Escola": "ESTGV"},
                "Contatos":  {"Telemovel": "961234567", "Mail": "carlosf@gmail.com"},
                "Morada":    {"Cidade": "Viseu", "CP": "3500-123"},
                "Notas":     {"Python": 18, "Sist. Operativos": 16, "Redes": 15}
            },
            "aluno_02": {
                "Estudante": {"Nome": "Carol", "Apelido": "Martins"},
                "CC": "87654321", 
                "Idade": 31,
                "Colocacao": {"Curso": "Artes Plásticas", "Escola": "ESAP"},
                "Contatos":  {"Telemovel": "912345678", "Mail": "carol.art@hotmail.com"},
                "Morada":    {"Cidade": "Lisboa", "CP": "1000-050"},
                "Notas":     {"Pintura": 19, "Escultura": 18, "História Arte": 17}
            },
            "aluno_03": {
                "Estudante": {"Nome": "Monica", "Apelido": "Tavares"},
                "CC": "11223344",
                "Idade": 34,
                "Colocacao": {"Curso": "Biologia", "Escola": "UBM"},
                "Contatos":  {"Telemovel": "933456789", "Mail": "monica.bio@sapo.pt"},
                "Morada":    {"Cidade": "Aveiro", "CP": "3800-200"},
                "Notas":     {"Genética": 14, "Botânica": 15, "Química": 16}
            }
        }

    def relatorio_geral(self):
        print("--- BASE DE DADOS ORGANIZADA ---")
        
        for id_aluno, dados in self.bd_escola.items():
            # Variáveis de atalho
            info_pessoal = dados['Estudante']
            info_curso = dados['Colocacao']
            info_contato = dados['Contatos']
            info_morada = dados['Morada']
            
            print(f"\nID SISTEMA: {id_aluno}")
            
            # Dados Pessoais
            nome_completo = f"{info_pessoal['Nome']} {info_pessoal['Apelido']}"
            print(f"Aluno: {nome_completo} (Idade: {dados['Idade']})")
            print(f"Doc. ID (CC): {dados['CC']}") 
            
            # Restante informação
            print(f"Curso: {info_curso['Curso']} @ {info_curso['Escola']}")
            print(f"Email: {info_contato['Mail']} | Tlm: {info_contato['Telemovel']}")
            print(f"Zona: {info_morada['Cidade']} ({info_morada['CP']})")
            
            print("Notas:")
            for disc, nota in dados['Notas'].items():
                print(f"   -> {disc}: {nota}")
            
            print("-" * 40)

# Execução
sistema = BaseDados()
sistema.relatorio_geral()