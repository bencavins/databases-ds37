import sqlite3
import queries


def connect_to_db(db_name):
    return sqlite3.connect(db_name)


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


if __name__ == '__main__':
    conn = connect_to_db('rpg_db.sqlite3')
    print(execute_query(conn, queries.select_all))