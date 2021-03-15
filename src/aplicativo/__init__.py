'''
modulo que abre a tela principal
'''

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.aplicativo.note_banco import NoteBanco


class Aplicativo:

    def __init__(self):
        # Acessa o arquivo glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file('src/tela/tela_principal_v1.glade')
        self.builder.connect_signals(self)
        self.banco = NoteBanco(self.builder)

        # Acessa a tela principal
        self.telaPrincipal = self.builder.get_object('tela_final')
        self.telaPrincipal.show()

    def note_foco(self, widget, none, null):
        self.banco.foco_banco()

    # Tela do Banco
    def banco_monta_cadastro(self, widget):
        self.banco.cadastro_banco()

    def banco_insert_cadastro(self, widget):
        self.banco.insert_cadastro_banco()

    # Fecha o programa
    def sairTelaPrincipal(self, widget):
        Gtk.main_quit()

    def main(self):
        Gtk.main()
