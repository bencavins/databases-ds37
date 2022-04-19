import sqlite3
import psycopg2
import queries


dbname = 'bdsizwly'
user = 'bdsizwly'
password = ''
host = 'rajje.db.elephantsql.com'


connection = psycopg2.connect(
    dbname=dbname, 
    user=user, 
    password=password, 
    host=host)

cursor = connection.cursor()


def pipe_data():
    sl_connection = sqlite3.connect('rpg_db.sqlite3')
    sl_cursor = sl_connection.cursor()

    character_data = sl_cursor.execute(queries.get_characters).fetchall()

    for row in character_data:
        insert_statement = f"""
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES
        {row[1:]}
        """
        cursor.execute(insert_statement)
    cursor.close()
    connection.commit()


def query_postgres():
    # cursor.execute(queries.create_character_table)
    # cursor.close()
    # connection.commit()

    cursor.execute(queries.get_characters)
    print(cursor.fetchall())


if __name__ == '__main__':
    # pipe_data()
    query_postgres()