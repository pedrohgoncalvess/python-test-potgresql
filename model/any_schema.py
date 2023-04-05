from types import FunctionType
from connection.connect import Db_connect
from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey


def create_table(func:FunctionType):
    meta = Db_connect()._meta
    engine = Db_connect()._engine
    def create(metadata:MetaData = meta):
        func(metadata)
        metadata.create_all(engine)
    return create


#TABLES

@create_table
def tb_test(metadata:MetaData):
    Table(
        'test',
        metadata,
        Column("nome", String(500)),
        Column("idade", Integer),
        schema='any_schema'
    )
