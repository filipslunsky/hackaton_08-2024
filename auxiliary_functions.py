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

def get_number_input(message):
    while True:    
        user_input = input(message)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            continue
    return user_input

def get_today_date(action):
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


if __name__ == "__main__":
    print(get_number_input("test:  "))
    print(get_today_date("test"))