'''
programa principal para abrir tela

'''

from src.aplicativo import Aplicativo as facade

if __name__ == '__main__':
    finan = facade()
    finan.main()
