create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived BOOLEAN,
    pclass INT,
    name VARCHAR(255),
    sex VARCHAR(24),
    age INT,
    sibs_spouse INT,
    parent_children INT,
    fare NUMERIC(10)
)
"""