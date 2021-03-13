# Conexao com o Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.util.variaveis import ConexaoBanco as VAR


class ConexaoPostgres:
    def __init__(self):
        POSTGRES_PSYCOPG2_ALCHEMY_URI = 'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'

        config = {"host": VAR.POSTGRES_HOST,
                  "port": int(VAR.POSTGRES_PORT),
                  "database": VAR.POSTGRES_DATABASE,
                  "user": VAR.POSTGRES_USER,
                  "password": VAR.POSTGRES_PASSWD}

        str_alchemy = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)

        self.conn = str_alchemy

    def conexao(self):
        engine = create_engine(self.conn)
        _conn = engine.connect()
        return _conn

    def session(self):
        _engine = create_engine(self.conn)
        Session = sessionmaker(bind=_engine)
        _session = Session()
        return _session
