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
        self.cadastro = self.builder.get_object('tela_banco_cadastro')
        self.cadastro.set_visible(False)
        self.img = self.builder.get_object('img_banco_tela')
        self.img.set_visible(True)
        self.img2 = self.builder.get_object('img_banco_logo')
        self.img2.set_visible(False)
        self.label_banco = self.builder.get_object('id_banco_label')
        self.label_banco.set_visible(False)
        self.vdd = False

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
        self.cadastro = self.builder.get_object('tela_banco_cadastro')
        self.cadastro.set_visible(True)
        self.img = self.builder.get_object('img_banco_tela')
        self.img.set_visible(False)
        self.img2 = self.builder.get_object('img_banco_logo')
        self.img2.set_visible(True)
        self.label_banco = self.builder.get_object('id_banco_label')
        self.label_banco.set_visible(True)
        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        self.limpar_dados()
        self.vdd = True

    def insert_cadastro_banco(self):
        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        try:
            if self.vdd:
                banco = Agencia()
                codigo = self.builder.get_object('txt_banco_codigo')
                banco.codigo_banco = int(codigo.get_text())
                nome = self.builder.get_object('txt_banco_nome')
                banco.nome = nome.get_text()
                agencia = self.builder.get_object('txt_banco_agencia')
                banco.agencia = int(agencia.get_text())
                conta = self.builder.get_object('txt_banco_conta')
                banco.conta = int(conta.get_text())
                tipo = self.builder.get_object('txt_banco_tipo')
                banco.tipo_conta = tipo.get_text()

                if banco.agencia and banco.codigo_banco and banco.nome and banco.tipo_conta != '':

                    self.session.add(banco)
                    self.session.commit()
                    self.session.query(Agencia)
                    self.mensagem.set_text('Dados inserido com sucesso')
                    self.limpar_dados()
                else:
                    self.abrirTelaDialogo(self.mensagem_aviso)

            else:
                self.abrirTelaDialogo('Favor clicar no botao cadastro')

        except Exception as err:
            self.mensagem_erro.set_text(f'Erro :\n {err}')
