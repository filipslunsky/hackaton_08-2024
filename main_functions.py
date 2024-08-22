from initialize import make_query

def get_number_input(message):
    while True:    
        user_input = input(message)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            continue
    return user_input
    
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


# create_user()

def log_exercise():
    exercise_type = input("What kind of exercise did you do?  ")
    exercise_reps = get_number_input("How many reps did you do per set?  ")
    exercise_sets = get_number_input("How many sets did you do overall?  ")
    exercise_year = get_number_input("Date of exercise - year?  ")
    exercise_month = get_number_input("Date of exercise - month?  ")
    exercise_day = get_number_input("Date of exercise - day?  ")
    exercise_date = f"{exercise_month}-{exercise_day}-{exercise_year}"

    query = f"""
INSERT INTO exercise (exercise_type, exercise_reps, exercise_sets, exercise_date) VALUES
('{exercise_type}', {exercise_reps}, '{exercise_sets}', '{exercise_date}')
"""
    make_query(query)

# log_exercise()

def log_food_intake():
    food_name = input("What type of food did you eat?  ")
    serving_size = get_number_input("How many grams did you eat?  ")
    calories = get_number_input("How many calories does it have?  ")
    food_year = get_number_input("Date of eating - year?  ")
    food_month = get_number_input("Date of eating - month?  ")
    food_day = get_number_input("Date of eating - day?  ")
    food_date = f"{food_month}-{food_day}-{food_year}"

    query = f"""
INSERT INTO food (food_name, serving_size, calories, food_date) VALUES
('{food_name}', {serving_size}, '{calories}', '{food_date}')
"""
    make_query(query)

# log_food_intake()