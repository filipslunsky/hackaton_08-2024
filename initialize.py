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


query_test = """
    CREATE TABLE test_stuff(
    test_id SERIAL PRIMARY KEY,
    test_name VARCHAR(50) NOT NULL
    )
    """


make_query(query_test)