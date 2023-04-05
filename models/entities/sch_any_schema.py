from types import FunctionType
from connection.connect import Db_connect
from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey

create_table = Db_connect().create_table

#TABLES
@create_table
def tb_test(metadata:MetaData):
    table1 = Table(
        'test',
        metadata,
        Column("name", String(500)),
        Column("age", Integer),
        schema='any_schema'
    )
@create_table
def tb_test_2(metadata:MetaData):
    table2 = Table(
        'test_2',
        metadata,
        Column("name_2", String(500)),
        Column("age_2", Integer),
        schema='any_schema'
    )

tb_test()