from auxiliary_functions import make_query, get_number_input, get_date, get_string_input, fetch_query_one
from calculations_calories import get_calories_burned, get_calories_for_food, calculate_total_calories
from calculations_user import get_age, get_gender, get_height, get_weight, get_user_id

email = "johny.doe@gmail.com"   # for testing purposes only
user_id = get_user_id(email)    # for testing purposes only

def create_user(email):
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    height = get_number_input("What is your height in cm?  ")
    weight = get_number_input("What is your weight in kg?  ")
    gender = get_string_input("What is your gender?  ", ["male", "female"])
    birth_year = get_number_input("What year were you born in?  ")
    birth_month = get_number_input("What is the number of the month you were born in?  ")
    birth_day = get_number_input("What is the number of the day you were born on?  ")
    birth_date = f"{birth_month}-{birth_day}-{birth_year}"
    
    query = f"""
INSERT INTO users (email, first_name, last_name, gender, height, weight, birth_date) VALUES
('{email}','{first_name}', '{last_name}','{gender}', {height}, '{weight}', '{birth_date}')
"""
    make_query(query)


def log_exercise(email):
    user_id = get_user_id(email)
    exercise_type = input("What kind of exercise did you do?  ")
    exercise_duration = get_number_input("How many miutes did you exercise?  ")
    exercise_date = get_date("do the exercise")
    height = get_height(user_id)
    weight = get_weight(user_id)
    age = get_age(user_id)
    gender = get_gender(user_id)
    calories_burned = get_calories_burned(exercise_type, exercise_duration, height, weight, age, gender)

    query = f"""
INSERT INTO exercise (exercise_type, exercise_duration, calories_burned, exercise_date, fk_user_id) VALUES
('{exercise_type}', {exercise_duration}, '{calories_burned}', '{exercise_date}', (SELECT user_id FROM users WHERE email = '{email}'))
"""
    make_query(query)


def log_food_intake(email):
    food = input("What type of food did you eat?  ")
    list_of_tuples = get_calories_for_food(food)
    food_and_calories = calculate_total_calories(list_of_tuples)
    food_date = get_date("eat the food")
    food_list = list(food_and_calories.keys())
    food_name = ", ".join(food_list)
    calories = sum(food_and_calories.values())

    query = f"""
INSERT INTO food (food_name, calories, food_date, fk_user_id) VALUES
('{food_name}', '{calories}', '{food_date}', (SELECT user_id FROM users WHERE email = '{email}'))
"""
    make_query(query)

def check_email(email):
    query = f"""
SELECT email FROM users WHERE email = '{email}';
"""
    results = fetch_query_one(query)
    if not results:
        return False
    else:
        return True


if __name__ == "__main__":
    # create_user()
    # log_exercise()
    # log_food_intake()
    print(check_email(email))
