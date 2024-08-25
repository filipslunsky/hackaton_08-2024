import psycopg2
from dotenv import load_dotenv
import os
import datetime

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

def fetch_query_one(query):
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
    results = cursor.fetchone()
    return results

def fetch_query_all(query):
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
    results = cursor.fetchall()
    return results

def get_number_input(message):
    while True:    
        user_input = input(message)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            continue
    return user_input

def get_string_input(message, valid_answers:list):
    while True:
        answer = input(message)
        if answer in valid_answers:
            break
    return answer


def get_date(action):
    while True:
        answer = input(f"Did you {action} today? (y/n):  ")
        if answer == "y":
            full_date = datetime.date.today()
            year = full_date.strftime("%Y")
            month = full_date.strftime("%m")
            day = full_date.strftime("%d")
            break
        elif answer == "n":
            year = get_number_input(f"When did you {action} - year?  ")
            month = get_number_input(f"When did you {action} - month?  ")
            day = get_number_input(f"When did you {action} - day?  ")
            break
    date = f"{month}-{day}-{year}"
    return date

def get_today_date():
    full_date = datetime.date.today()
    return full_date


if __name__ == "__main__":
    print(get_number_input("test:  "))
    print(get_date("test"))
    print(get_string_input("Are you (m)ale or (f)emale?  ", ["m", "f"]))