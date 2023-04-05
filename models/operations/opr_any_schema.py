import inspect
import os
from configs.environment_variables import get_environment_variables as env
from types import FunctionType
from connection.connect import Db_connect
from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey

def tb_test_2(metadata:MetaData):
    Teste = Table(
        'test_2',
        metadata,
        Column("name_2", String(500)),
        Column("age_2", Integer),
        schema='any_schema'
    )

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


