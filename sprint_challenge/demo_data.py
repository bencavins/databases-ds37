import sqlite3


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(1),
    x INT,
    y INT
);
"""


def create_sqlite_connection(db_name='demo_data.sqlite3'):
    connection = sqlite3.connect(db_name)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    return cursor.execute(query).fetchall()


def execute_data_update(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.commit()


