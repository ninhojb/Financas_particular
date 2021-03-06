from datetime import datetime

from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR,REAL
from sqlalchemy.ext.declarative import declarative_base

AlchemyEntity = declarative_base()


class Agencia(AlchemyEntity):
    __tablename__ = 'banco'
    __table_args__ = {"schema": "fin"}

    id_banco = Column(Integer, primary_key=True, autoincrement=True)
    codigo_banco = Column(Integer)
    nome = Column(VARCHAR)
    agencia = Column(Integer)
    conta = Column(Integer)
    tipo_conta = Column(VARCHAR)
    dt_ingestao = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"

class BancoSaldo(AlchemyEntity):
    __tablename__ = 'banco_saldo'
    __table_args__ = {'schema': 'fin'}

    id_banco_saldo = Column(Integer, primary_key=True, autoincrement=True)
    id_banco = Column(Integer)
    agencia = Column(Integer)
    conta = Column(Integer)
    saldo = Column(REAL)
    dt_saldo = Column(TIMESTAMP)
    dt_ingestao = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"
