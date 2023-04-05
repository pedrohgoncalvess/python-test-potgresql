class Db_connect():
    def __init__(self):
        from sqlalchemy import create_engine, schema,MetaData
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

    #EXECUTE INSERT, UPDATE, DELETE COMMANDS
    def exec_dml_com(self,query):
        with self._engine.connect() as conn:
            conn.execute(query)

