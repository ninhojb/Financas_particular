from abc import ABC


class Constantes(ABC):
    BLANK = ''


class ConexaoBanco:
    POSTGRES_HOST = 'localhost'
    POSTGRES_PORT = '5432'
    POSTGRES_USER = 'financa'
    POSTGRES_PASSWD = 'financa'
    POSTGRES_DATABASE = 'financa'
