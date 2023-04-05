from types import FunctionType
from typing import Any

from sqlalchemy import MetaData,create_engine, schema

class Db_connect():

    def __init__(self):
        from configs.environment_variables import get_environment_variables as env
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker


        #CREATE ENGINE AND CONNECT WITH DATABASE
        engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host_name')}/{env('database_name')}",
                               echo=True)
        Base = declarative_base()
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()


        # CREATE SCHEMAS IF NOT EXIST
        schemas = ['any_schema']
        for schemaName in schemas:
            if not engine.dialect.has_schema(engine, schemaName):
                engine.execute(schema.CreateSchema(schemaName))

        self._engine = engine
        self._base = Base
        self._meta = MetaData()
        self._session = session
        self._write_represent = Create_representation()

    #EXECUTE INSERT, UPDATE, DELETE COMMANDS
    def exec_dml_com(self,query:Any):
        with self._engine.connect() as conn:
            conn.execute(query)


    #CREATE TABLES
    def create_table(self, table):
        import inspect
        meta = self._meta
        engine = self._engine
        write = self._write_represent
        textFunc = inspect.getsource(table)
        write.rewrite_table(textFunc)
        def create(metadata: MetaData = meta):
            table(metadata)
            metadata.create_all(engine)

        return create


#CREATE REPRESENTATION OF TABLES TO PERFORM OPERATIONS WITH SQLALCHEMY AND NOT JUST SQL RAW
class Representation():
    def __init__(self):
        from configs.environment_variables import get_environment_variables as env
        import os

        try:
            with open(os.path.join(env("main_dir") + "\\models", "representation.py"), "r") as f:
                if f.find("import") == -1:
                    with open(os.path.join(env("main_dir") + "\\models", "representation.py"), "w") as f:
                        f.write("""from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey
                                    """)
        except:
            with open(os.path.join(env("main_dir") + "\\models", "representation.py"), "w") as f:
                f.write("""from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey
                            """)

    def rewrite_table(self,text):
        import os
        from configs.environment_variables import get_environment_variables as env

        representationTable = (text.split("):")[1].replace("    ", "").replace("metadata,","").replace("\n",""))

        with open(os.path.join(env("main_dir") + "/models", "representation.py"), "r") as f:
            text = f.read()
        if text.find(representationTable) == -1:
            with open(os.path.join(env("main_dir") + "/models", "representation.py"), "a") as f:
                f.write("\n" + representationTable)
