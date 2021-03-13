class NoteBanco:
    def __init__(self):
        pass

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
