from auxiliary_functions import make_query, get_number_input, get_today_date

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
    exercise_reps = get_number_input("How many reps did you do per set?  ")
    exercise_sets = get_number_input("How many sets did you do overall?  ")
    exercise_date = get_today_date("do the exercise")

    query = f"""
INSERT INTO exercise (exercise_type, exercise_reps, exercise_sets, exercise_date) VALUES
('{exercise_type}', {exercise_reps}, '{exercise_sets}', '{exercise_date}')
"""
    make_query(query)


def log_food_intake():
    food_name = input("What type of food did you eat?  ")
    serving_size = get_number_input("How many grams did you eat?  ")
    calories = get_number_input("How many calories does it have?  ")
    food_date = get_today_date("eat the food")

    query = f"""
INSERT INTO food (food_name, serving_size, calories, food_date) VALUES
('{food_name}', {serving_size}, '{calories}', '{food_date}')
"""
    make_query(query)

if __name__ == "__main__":
    create_user()
    log_exercise()
    log_food_intake()

def convert_food_to_calories():
    pass

def convert_exercise_to_calories():
    pass

def get_daily_exercise_quote():
    pass

def get_daily_calories_quote():
    pass
