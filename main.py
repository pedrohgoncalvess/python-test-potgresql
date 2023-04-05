from connection import Db_connect

conn = Db_connect()

conn.exec_dml_com("insert into any_schema.test values ('Pedro',15)")