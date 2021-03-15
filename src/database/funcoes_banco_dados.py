# onde coloco as pequisas


import logging

from psycopg2 import DatabaseError

from src.database.tabelas import Tabela


class FuncBanco:

    def __init__(self):
        conn = Tabela()
        self.conn = conn.conexao
        self.session = conn.session

    def executar_insert(self, sql):
        logging.info('[EXECUTAR_INSERT]')
        _conn = self.conn
        try:
            resul = _conn.execute(sql)

            return 'Inserido com sucesso'

        except (Exception, DatabaseError) as error:
            return print(error)

    def executar_select(self, sql):
        logging.info('[EXECUTAR_SELECT]')
        _conn = self.conn
        try:

            resul = _conn.execute(sql)

            return 'Select com sucesso'

        except (Exception, DatabaseError) as error:
            return logging.info(error)

    def session(self):
        return self.session
