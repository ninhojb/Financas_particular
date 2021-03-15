from datetime import date

from gi.repository import Gtk

from src.database.funcoes_banco_dados import FuncBanco
from src.database.persistencia.schema_fin import Agencia


class NoteBanco:
    def __init__(self, builder):
        self.func = FuncBanco()
        today = date.today()
        self.session = self.func.session
        self.hoje = today.strftime('%Y-%m-%d')
        self.builder = builder
        self.mensagem = self.builder.get_object('txt_banco_mensagem')
        self.mensagem_erro = self.builder.get_object('txt_banco_erro')
        self.mensagem_aviso = 'Favor preecher todos os dados'

    def foco_banco(self):
        self.novo = self.builder.get_object('tela_banco_cadastro')
        self.novo.set_visible(False)
        self.img = self.builder.get_object('img_banco_tela')
        self.img.set_visible(True)
        self.img2 = self.builder.get_object('img_banco_logo')
        self.img2.set_visible(False)
        self.label_banco = self.builder.get_object('id_banco_label')
        self.label_banco.set_visible(False)
        self.tela_cadastro = False
        self.tela_novo = False

    def limpar_dados(self):
        # limpa a tela de cadasto
        codigo = self.builder.get_object('txt_banco_codigo')
        codigo.set_text('')
        nome = self.builder.get_object('txt_banco_nome')
        nome.set_text('')
        agencia = self.builder.get_object('txt_banco_agencia')
        agencia.set_text('')
        conta = self.builder.get_object('txt_banco_conta')
        conta.set_text('')
        tipo = self.builder.get_object('txt_banco_tipo')
        tipo.set_text('')

    def abrirTelaDialogo(self, msn):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, "Aviso!")
        dialog.format_secondary_text(msn)
        dialog.run()
        dialog.destroy()

    def cadastro_banco(self):
        # Desativa o a imagem e monta os dados
        self.novo = self.builder.get_object('tela_banco_cadastro')
        self.novo.set_visible(True)
        self.novo = self.builder.get_object('tela_banco_novo')
        self.novo.set_visible(False)
        self.img = self.builder.get_object('img_banco_tela')
        self.img.set_visible(False)
        self.img2 = self.builder.get_object('img_banco_logo')
        self.img2.set_visible(True)
        self.label_banco = self.builder.get_object('id_banco_label')
        self.label_banco.set_visible(True)
        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        self.limpar_dados()
        self.tela_cadastro = True
        self.tela_novo = False

    def cadastro_novo(self):
        # Desativa o a imagem e monta os dados
        self.novo = self.builder.get_object('tela_banco_novo')
        self.novo.set_visible(True)
        self.novo = self.builder.get_object('tela_banco_cadastro')
        self.novo.set_visible(False)
        self.img = self.builder.get_object('img_banco_tela')
        self.img.set_visible(False)
        self.img2 = self.builder.get_object('img_banco_logo')
        self.img2.set_visible(True)
        self.label_banco = self.builder.get_object('id_banco_label')
        self.label_banco.set_visible(True)
        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        self.limpar_dados()
        self.tela_cadastro = False
        self.tela_novo =True

    def insert_cadastro_novo(self):
        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        if self.tela_cadastro or self.tela_novo:
            self.banco = Agencia()
            codigo = self.builder.get_object('txt_banco_codigo')
            self.banco.codigo_banco = codigo.get_text()
            nome = self.builder.get_object('txt_banco_nome')
            self.banco.nome = nome.get_text()
            agencia = self.builder.get_object('txt_banco_agencia')
            self.banco.agencia = agencia.get_text()
            conta = self.builder.get_object('txt_banco_conta')
            self.banco.conta = conta.get_text()
            tipo = self.builder.get_object('txt_banco_tipo')
            self.banco.tipo_conta = tipo.get_text()
        else:
            self.abrirTelaDialogo('Favor clicar no botao cadastro')

        if self.banco.agencia and self.banco.codigo_banco and self.banco.nome and self.banco.tipo_conta != '':
            try:
                self.banco.codigo_banco = int(self.banco.codigo_banco)
                self.banco.agencia = int(self.banco.agencia)
                self.banco.conta = int(self.banco.conta)
                self.session.add(self.banco)
                self.session.commit()
                self.session.query(Agencia)
                self.mensagem.set_text('Dados inserido com sucesso')
                self.limpar_dados()

            except Exception as err:
                self.mensagem_erro.set_text(f'Erro :\n {err}')

        else:
            self.abrirTelaDialogo(self.mensagem_aviso)


    def inserir_d(self):
        pass