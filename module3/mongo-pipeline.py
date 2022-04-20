import pymongo
import sqlite3


select_all = """
SELECT * 
FROM charactercreator_character;
"""


SELECT_ITEM_FOR_CHARACTER = """
SELECT *
FROM charactercreator_character_inventory as i 
LEFT JOIN armory_item as ai
	ON i.item_id = ai.item_id
WHERE i.character_id = 1;
"""


def create_mdb_connection(collection_name):
    client = pymongo.MongoClient(
    "mongodb+srv://bencavins:C@cluster0.2vdvn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    db = client.test
    collection = db[collection_name]
    return db


def create_sqlite_connection(db_name='rpg_db.sqlite3'):
    connection = sqlite3.connect(db_name)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    # import pdb; pdb.set_trace()
    return cursor.execute(query).fetchall()


def character_tuple_to_dict(characters):
    dict_list = []
    for character in characters:
        character_doc = {
            'character_id': character[0],
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8],
        }
        dict_list.append(character_doc)
    return dict_list


def query_character_items(connection, characters):
    for character in characters:
        character_id = character['character_id']
        query = f"""
SELECT *
FROM charactercreator_character_inventory as i 
LEFT JOIN armory_item as ai
	ON i.item_id = ai.item_id
WHERE i.character_id = {character_id};
"""
        items_tuples = execute_query(connection, query)
        items_list = []
        for item in items_tuples:
            item_doc = {
                'item_id': item[3],
                'name': item[4],
                'value': item[5],
                'weight': item[6]
            }
            items_list.append(item_doc)
        character['items'] = items_list
    return characters


def insert_characters(db, characters):
    db.characters.insert_many(characters)


if __name__ == '__main__':
    db = create_mdb_connection('characters')
    sl_conn = create_sqlite_connection()
    characters_list = execute_query(sl_conn, select_all)
    character_docs = character_tuple_to_dict(characters_list)
    query_character_items(sl_conn, character_docs)
    insert_characters(db, character_docs)

    print(db.characters.find_one({}))
    # db.characters.delete_many({})