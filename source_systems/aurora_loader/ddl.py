from .connection import engine

DDL = """

CREATE SCHEMA IF NOT EXISTS netflix;

"""

def create_schema():

    with engine.begin() as conn:
        conn.exec_driver_sql(DDL)

    print("Schema Created")