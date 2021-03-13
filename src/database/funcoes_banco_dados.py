# onde coloco as pequisas


import logging

from psycopg2 import DatabaseError


class FuncBanco:

    def __init__(self):
        pass

    def executar_insert(self, database, sql):
        logging.info('[EXECUTAR_INSERT]')
        _conn = database
        try:
            resul = _conn.execute(sql)

            return 'Inserido com sucesso'

        except (Exception, DatabaseError) as error:
            return print(error)

    def executar_select(self, database, sql):
        logging.info('[EXECUTAR_SELECT]')
        _conn = database
        try:

            resul = _conn.execute(sql)

            return 'Select com sucesso'

        except (Exception, DatabaseError) as error:
            return logging.info(error)
