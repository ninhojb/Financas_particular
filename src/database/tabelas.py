# Cria as tabelas


from src.database import ConexaoPostgres


class Tabela:

    def __init__(self):
        conn = ConexaoPostgres()
        self.conexao = conn.conexao()
        self.session = conn.session()
        self.criar_tabela_banco()
        self.criar_tabela_banco_saldo()

    def criar_tabela_banco(self):
        self.conexao.execute('''
            CREATE TABLE if not exists fin.banco (
                id_banco SERIAL NOT NULL PRIMARY KEY ,
                codigo_banco int NOT NULL,
                nome varchar NOT NULL,
                agencia int NOT NULL,
                conta int NOT NULL,
                tipo_conta varchar NOT NULL,
                dt_ingestao date DEFAULT current_date
                );
        ''')
        return 'tabela cadastro banco criada com sucesso'

    def criar_tabela_banco_saldo(self):
        self.conexao.execute('''
            CREATE TABLE if not exists fin.banco_saldo (
               id_banco_saldo SERIAL NOT NULL PRIMARY KEY ,
               id_banco int NOT NULL,
               agencia int NOT NULL,
               conta int NOT NULL,
               saldo real  NOT NULL,
               dt_saldo date NOT NULL,
               dt_ingestao date DEFAULT current_date
               );
            ''')
        return 'tabela cadastro banco_saldo criada com sucesso'
