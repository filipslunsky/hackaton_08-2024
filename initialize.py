# running the script in this file will create a local version of postgres database tables on your machine
from auxiliary_functions import make_query

query1 = """
    CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(70) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
	gender VARCHAR(255) NOT NULL,
	height SMALLINT,
	weight SMALLINT,
    birth_date DATE
);
    """

query2 = """
CREATE TABLE exercise (
    exercise_id SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    exercise_duration DECIMAL,
    calories_burned DECIMAL,
    exercise_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""

query3 = """
CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255),
    calories DECIMAL,
    food_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user_food FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""
if __name__ == "__main__":
    make_query(query1)
    print("users table successfully created")
    make_query(query2)
    print("exercise table successfully created")
    make_query(query3)
    print("food table successfully created")
    print("all 3 neccessary tables created")