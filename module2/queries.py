select_all = """
SELECT * 
FROM charactercreator_character;
"""

TOTAL_CHARACTERS = """
select count(*)
from charactercreator_character;
"""

TOTAL_THEIF = """
SELECT count(*)
FROM charactercreator_character as c
JOIN charactercreator_thief as t 
		ON c.character_id = t.character_ptr_id;
"""

TOTAL_NON_WEAPONS = """
SELECT count(*)
FROM charactercreator_character as c
JOIN charactercreator_thief as t 
		ON c.character_id = t.character_ptr_id;
"""

AVG_ITEMS_PER_CHARACTER = """
SELECT AVG(total_items)
FROM
(
SELECT c.character_id, c.name, COUNT(*) as total_items
FROM charactercreator_character as c
JOIN charactercreator_character_inventory as ci
	ON c.character_id = ci.character_id
GROUP BY c.character_id, c.name
);
"""


get_characters = """
SELECT * FROM charactercreator_character;
"""


create_character_table = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
)
"""