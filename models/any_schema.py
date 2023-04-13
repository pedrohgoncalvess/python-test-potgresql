from connection.connect import Db_connect
from sqlalchemy import func
from sqlalchemy import Column,Integer,String,Date, MetaData, Table, ForeignKey

engine = Db_connect()._engine
metadata = MetaData()

#ANY_SCHEMA TABLES

table_person = Table(
    'test_person',
    metadata,
    Column("name", String(50)),
    Column("age", Integer),
    Column("job",String(50), nullable=False),
    Column("inserted_at",Date,server_default=func.now()),
    schema='any_schema'
)

table_prod = Table(
        'test_prod',
        metadata,
        Column("id",Integer,autoincrement=True,primary_key=True),
        Column("prod_name", String(30)),
        Column("ind_name",String(20)),
        Column("quantity", Integer),
        schema='any_schema'
    )

metadata.create_all(engine)