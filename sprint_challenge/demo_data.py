import sqlite3


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(1),
    x INT,
    y INT
);
"""

INSERT_DATA = """
INSERT INTO demo 
(s, x, y)
VALUES
("g", 3, 9),
("v", 5, 7),
("f", 8, 7);
"""

COUNT_ROWS = """
SELECT COUNT(*)
FROM demo;
"""

COUNT_XY_AT_LEAST_5 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;
"""

COUNT_DISTINCT_Y = "SELECT COUNT(DISTINCT y) FROM demo;"


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


sl_conn = create_sqlite_connection()
execute_data_update(sl_conn, CREATE_TABLE)
# execute_data_update(sl_conn, INSERT_DATA)
row_count = execute_query(sl_conn, COUNT_ROWS)
xy_at_least_5 = execute_query(sl_conn, COUNT_XY_AT_LEAST_5)
unique_y = execute_query(sl_conn, COUNT_DISTINCT_Y)


expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

avg_hire_age = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""

ten_most_expensive = """
SELECT p.ProductName, p.UnitPrice, s.CompanyName
FROM Product as p
JOIN Supplier as s
	ON s.Id = p.SupplierId
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""