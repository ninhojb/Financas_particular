from src.database.tabelas import Tabela
from src.database.funcoes_banco_dados import FuncBanco
from datetime import date
from src.database import ConexaoPostgres

class NoteBanco:
    def __init__(self):
        database = ConexaoPostgres()
        self.database = database.conexao()
        self.func = FuncBanco()
        today = date.today()
        self.hoje = today.strftime('%Y-%m-%d')


    def foco_banco(self, builder):
        self.cadastro = builder.get_object('tela_banco_cadastro')
        self.cadastro.set_visible(False)
        self.img = builder.get_object('img_banco_tela')
        self.img.set_visible(True)
        self.img2 = builder.get_object('img_banco_logo')
        self.img2.set_visible(False)
        self.label_banco = builder.get_object('id_banco_label')
        self.label_banco.set_visible(False)

    def cadastro_banco(self, builder):
        # Desativa o a imagem e monta os dados
        self.cadastro = builder.get_object('tela_banco_cadastro')
        self.cadastro.set_visible(True)
        self.img = builder.get_object('img_banco_tela')
        self.img.set_visible(False)
        self.img2 = builder.get_object('img_banco_logo')
        self.img2.set_visible(True)
        self.label_banco = builder.get_object('id_banco_label')
        self.label_banco.set_visible(True)

    def insert_cadastro_banco(self, builder):
        codigo = 341
        dt_ingestao = self.hoje
        nome = builder.get_object('txt_banco_nome')
        nome = nome.get_text()
        agencia = builder.get_object('txt_banco_agencia')
        agencia = agencia.get_text()
        conta = builder.get_object('txt_banco_conta')
        conta= int(conta.get_text())
        tipo = builder.get_object('txt_banco_tipo')
        tipo = str(tipo.get_text())
        sql = F'''
                INSERT INTO fin.banco
                    (codigo_banco,nome,agencia,conta,tipo_conta)
                    VALUES({codigo},'{nome}',{agencia},{conta},'{tipo}')
        '''
        print(sql)
        insert = self.func.executar_insert(self.database, sql)
        return insert
