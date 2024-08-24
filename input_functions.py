from auxiliary_functions import make_query, get_number_input, get_date
from calculations_calories import get_calories_burned, get_calories_for_food, calculate_total_calories
from calculations_user import get_age, get_gender, get_height, get_weight

def create_user():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    height = get_number_input("What is your height in cm?  ")
    weight = get_number_input("What is your weight in kg?  ")
    birth_year = get_number_input("What year were you born in?  ")
    birth_month = get_number_input("What is the number of the month you were born in?  ")
    birth_day = get_number_input("What is the number of the day you were born on?  ")
    birth_date = f"{birth_month}-{birth_day}-{birth_year}"
    
    query = f"""
INSERT INTO users (first_name, last_name, height, weight, birth_date) VALUES
('{first_name}', '{last_name}', {height}, '{weight}', '{birth_date}')
"""
    make_query(query)


def log_exercise():
    exercise_type = input("What kind of exercise did you do?  ")
    exercise_duration = get_number_input("How many miutes did you exercise?  ")
    exercise_date = get_date("do the exercise")
    height = get_height()
    weight = get_weight()
    age = get_age()
    gender = get_gender()
    calories_burned = get_calories_burned(exercise_type, exercise_duration, height, weight, age, gender)

    query = f"""
INSERT INTO exercise (exercise_type, exercise_reps, exercise_sets, exercise_date) VALUES
('{exercise_type}', {exercise_duration}, '{calories_burned}', '{exercise_date}')
"""
    make_query(query)


def log_food_intake():
    food = input("What type of food did you eat?  ")
    list_of_tuples = get_calories_for_food(food)
    food_and_calories = calculate_total_calories(list_of_tuples)
    food_date = get_date("eat the food")
    serving_size = 0
    food_list = list(food_and_calories.keys())
    food_name = ", ".join(food_list)
    calories = sum(food_and_calories.values())

    query = f"""
INSERT INTO food (food_name, serving_size, calories, food_date) VALUES
('{food_name}', {serving_size}, '{calories}', '{food_date}')
"""
    make_query(query)

if __name__ == "__main__":
    create_user()
    log_exercise()
    log_food_intake()
