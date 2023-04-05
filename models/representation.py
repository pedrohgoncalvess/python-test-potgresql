from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey
                            
table1 = Table('test',Column("name", String(500)),Column("age", Integer),schema='any_schema')
table2 = Table('test_2',Column("name_2", String(500)),Column("age_2", Integer),schema='any_schema')