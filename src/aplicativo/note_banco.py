from datetime import date

from gi.repository import Gtk

from src.database.funcoes_banco_dados import FuncBanco
from src.database.persistencia.schema_fin import Agencia, BancoSaldo


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
        self.id_banco = 1

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

        agencia_novo = self.builder.get_object('txt_banco_novo_agencia')
        agencia_novo.set_text('')
        conta_novo = self.builder.get_object('txt_banco_novo_conta')
        conta_novo.set_text('')
        saldo_novo = self.builder.get_object('txt_banco_novo_saldo')
        saldo_novo.set_text('')
        data_novo = self.builder.get_object('txt_banco_novo_data')
        data_novo.set_text('')

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
        self.comboNovoBanco()
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
        self.tela_cadastro = False
        self.tela_novo = True

    def insert_cadastro_novo(self):
        if not self.tela_cadastro and not self.tela_novo:
            self.abrirTelaDialogo('Favor clicar no botao cadastro ou novo')

        self.mensagem.set_text('')
        self.mensagem_erro.set_text('')
        if self.tela_cadastro:
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

            if self.banco.agencia and self.banco.codigo_banco and self.banco.nome and self.banco.tipo_conta != '':
                try:
                    self.banco.codigo_banco = int(self.banco.codigo_banco)
                    self.banco.agencia = int(self.banco.agencia)
                    self.banco.conta = int(self.banco.conta)
                    self.session.add(self.banco)
                    self.session.commit()
                    self.mensagem.set_text('Dados inserido com sucesso')
                    self.limpar_dados()


                except Exception as err:
                    self.abrirTelaDialogo(f'Erro :\n {err}')

            else:
                self.abrirTelaDialogo(self.mensagem_aviso)

        if self.tela_novo:
            self.saldo = BancoSaldo()

            agencia = self.builder.get_object('txt_banco_novo_agencia')
            self.saldo.agencia = agencia.get_text()
            conta = self.builder.get_object('txt_banco_novo_conta')
            self.saldo.conta = conta.get_text()
            saldo = self.builder.get_object('txt_banco_novo_saldo')
            self.saldo.saldo = saldo.get_text()
            data = self.builder.get_object('txt_banco_novo_data')
            self.saldo.dt_saldo = data.get_text()
            self.saldo.id_banco = self.id_banco

            if self.saldo.agencia and self.saldo.conta and self.saldo.saldo and self.saldo.dt_saldo != '':
                try:
                    self.saldo.id_banco = int(self.saldo.id_banco)
                    self.saldo.agencia = int(self.saldo.agencia)
                    self.saldo.conta = int(self.saldo.conta)

                    self.session.add(self.saldo)
                    self.session.commit()
                    self.abrirTelaDialogo('Dados inserido com sucesso')
                    self.limpar_dados()
                except Exception as err:
                    self.abrirTelaDialogo(err)
            else:

                self.abrirTelaDialogo(self.mensagem_aviso)

    # Funçao editar
    def banco_editar(self):
        self.telaLocalizar = self.builder.get_object('tela_localizar')
        self.telaLocalizar.show()

    def localizar_ok(self):
        codigo = self.builder.get_object('id_localizar_txt')
        self.codigo = codigo.get_text()

        if self.tela_cadastro:
            sql = self.session.query(Agencia) \
                .filter(Agencia.id_banco == self.codigo)

            for dados in sql:
                print(dados.codigo_banco, dados.nome, dados.agencia, dados.conta, dados.tipo_conta)
                codigo = self.builder.get_object('txt_banco_codigo')
                codigo.set_text(str(dados.codigo_banco))
                nome = self.builder.get_object('txt_banco_nome')
                nome.set_text(dados.nome)
                agencia = self.builder.get_object('txt_banco_agencia')
                agencia.set_text(str(dados.agencia))
                conta = self.builder.get_object('txt_banco_conta')
                conta.set_text(str(dados.conta))
                tipo = self.builder.get_object('txt_banco_tipo')
                tipo.set_text(dados.tipo_conta)

        elif self.tela_novo:
            sql = self.session.query(BancoSaldo) \
                .filter(BancoSaldo.id_banco_saldo == self.codigo)

            for dados in sql:
                print(dados.id_banco, dados.agencia, dados.conta, dados.saldo, dados.dt_saldo)

        self.telaLocalizar.hide_on_delete()

    def comboNovoBanco(self):
        self.valor_combo = self.builder.get_object('combo_banco_novo')
        self.listaStoreComboNovo = Gtk.ListStore(int, int)

        self.listaStoreComboNovo.clear()
        combo = self.session.query(Agencia.id_banco, Agencia.codigo_banco)

        for linha in combo:
            self.listaStoreComboNovo.append(linha)

        self.valor_combo.set_model(self.listaStoreComboNovo)
        self.valor_combo.connect('changed', self.on_name_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.valor_combo.pack_start(renderer_text, True)
        self.valor_combo.add_attribute(renderer_text, "text", 1)

    def on_name_combo_changed(self, combo):
        self.saldo = BancoSaldo()
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.id_banco, codigo_banco = model[tree_iter][:2]
            dados = self.session.query(Agencia) \
                .filter(Agencia.id_banco == self.id_banco)

            for linha in dados:
                agencia = self.builder.get_object('txt_banco_novo_agencia')
                self.saldo.agencia = agencia.set_text(str(linha.agencia))

                conta = self.builder.get_object('txt_banco_novo_conta')
                self.saldo.conta = conta.set_text(str(linha.conta))

        else:
            entry = combo.get_child()
