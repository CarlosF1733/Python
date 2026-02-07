import os
os.system('cls' if os.name == 'nt' else 'clear')

# Garante que a pasta existe
os.makedirs("Treino", exist_ok=True)

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

    def relatorio_inteligente(self):
        caminho_ficheiro = "Treino/alunos.txt"
        
        # 1. SCANNER: Ler o que já existe no ficheiro
        conteudo_existente = ""
        if os.path.exists(caminho_ficheiro):
            with open(caminho_ficheiro, "r", encoding="utf-8") as f_leitura:
                conteudo_existente = f_leitura.read()
        
        print("--- A PROCESSAR BASE DE DADOS ---")

        for id_aluno, dados in self.bd_escola.items():
            
            # --- PASSO A: PREPARAR OS DADOS (Sempre) ---
            info_pessoal = dados['Estudante']
            info_curso = dados['Colocacao']
            info_contato = dados['Contatos']
            info_morada = dados['Morada']

            # Criamos a lista AGORA para poder usá-la no print e no write
            linhas_formatadas = [
                f"{id_aluno} ------------------",
                f"{info_pessoal['Nome']} {info_pessoal['Apelido']}", 
                f"Idade: {dados['Idade']} anos",
                f"CC: {dados['CC']}", 
                f"Curso: {info_curso['Curso']}", 
                f"Escola: {info_curso['Escola']}",
                f"Email: {info_contato['Mail']}",
                f"Tlm: {info_contato['Telemovel']}",
                f"Morada: {info_morada['Cidade']} ({info_morada['CP']})",
                "-" * 28
            ]

            # --- PASSO B: MOSTRAR NO MONITOR (Sempre) ---
            # Aqui satisfazemos o teu pedido: aparece sempre no ecrã!
            print(f"\nDados em memória para: {info_pessoal['Nome']}")
            for linha in linhas_formatadas:
                print(linha)

            # --- PASSO C: DECIDIR SE GRAVA (Só se for novo) ---
            cc_para_verificar = f"CC: {dados['CC']}"

            if cc_para_verificar in conteudo_existente:
                # Se já existe, avisamos mas NÃO gravamos
                print(f" >> [INFO] Este CC já está no ficheiro. Gravação cancelada para evitar duplicados.")
            else:
                # Se é novo, gravamos
                print(f" >> [NOVO] A adicionar ao ficheiro...")
                with open(caminho_ficheiro, "a", encoding="utf-8") as f_escrita:
                    for linha in linhas_formatadas:
                        f_escrita.write(linha + "\n")
                
                # Atualizamos a memória local para apanhar duplicados na mesma execução
                conteudo_existente += cc_para_verificar

# Execução
sistema = BaseDados()
sistema.relatorio_inteligente()