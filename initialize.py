# running the script in this file will create a local version of postgres database tables on your machine

import psycopg2
from dotenv import load_dotenv
import os

def make_query(query):
    load_dotenv()
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')

    connection = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT)
        
    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()


query1 = """
    CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    weight VARCHAR(255)
);
    """

query2 = """
CREATE TABLE exercise (
    exercise_id SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    exercise_reps VARCHAR(255),
    exercise_sets VARCHAR(255),
    exercise_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
"""

query3 = """
CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255),
    serving_size VARCHAR(255),
    calories VARCHAR(255),
    food_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user_food FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
"""

make_query(query1)
make_query(query2)
make_query(query3)
