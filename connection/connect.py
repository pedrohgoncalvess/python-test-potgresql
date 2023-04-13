from typing import Any
from sqlalchemy import MetaData,create_engine, schema
from sqlalchemy.engine import CursorResult

class Db_connect():

    def __init__(self):
        from configs.environment_variables import get_environment_variables as env
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker


        #CREATE ENGINE AND CONNECT WITH DATABASE
        engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host')}:{env('port')}/{env('database_name')}",
                               echo=True)
        Base = declarative_base()
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()


        # CREATE SCHEMAS
        schemas = ['any_schema']
        for schemaName in schemas:
            if not engine.dialect.has_schema(engine, schemaName):
                engine.execute(schema.CreateSchema(schemaName))

        self._engine = engine
        self._base = Base
        self._meta = MetaData()
        self._session = session

    #EXECUTE INSERT, UPDATE, DELETE COMMANDS
    def exec_dml_com(self,query:Any):
        with self._engine.connect() as conn:
            conn.execute(query)

    #EXECUTE CONSULT COMMANDS
    def exec_dql_comm(self,query:Any) -> CursorResult:
        with self._engine.connect() as conn:
            result = conn.execute(query)
        return result


    #CREATE TABLES
    def create_table(self):
        from models import any_schema
        any_schema.metadata