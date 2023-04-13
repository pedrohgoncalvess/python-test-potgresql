import pytest
from connection import Db_connect
from sqlalchemy import insert
from models.any_schema import table_prod, table_person

conn = Db_connect()

def test_person_valid():

    fields_table_person = {
        "name" : "Pedro H",
        "age" : 20,
        "job" : "data eng"
    }

    queryTablePerson = insert(table_person).values(
        name=fields_table_person.get("name"),
        age=fields_table_person.get("age"),
        job=fields_table_person.get("job")
    )

    conn.exec_dml_com(queryTablePerson)



def test_prod_valid():

    fields_table_prod = {
        "prod_name" : "dor flex",
        "quantity" : 1500,
        "ind_name" : "ems generics"
    }
    queryTableProd = insert(table_prod).values(
        prod_name=fields_table_prod.get("prod_name"),
        quantity=fields_table_prod.get("quantity"),
        ind_name = fields_table_prod.get("ind_name")
    )

    conn.exec_dml_com(queryTableProd)



def test_person_result():
    query = """
    select * from any_schema.test_person where name = 'Pedro H'
    """
    result = conn.exec_dql_comm(query)
    for person in result:
        name = person.name
        age = person.age
        job = person.job

    assert name != "Pedro"
    assert age == 20
    assert job == 'data eng'


def test_multiples_inserts():
    fields_table_prod = {
        "prod_name" : "dor flex",
        "quantity" : 1500,
        "ind_name" : "ems generics"
    }

    queryTableProd = insert(table_prod).values(
        prod_name=fields_table_prod.get("prod_name"),
        quantity=fields_table_prod.get("quantity"),
        ind_name = fields_table_prod.get("ind_name")
    )

    for i in list(range(500)):
        conn.exec_dml_com(queryTableProd)



