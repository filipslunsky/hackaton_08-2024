from auxiliary_functions import fetch_query_one, get_today_date

# needs a parameter for specific users
def get_age():
    query = f"""
    SELECT birth_date
    FROM users
    WHERE user_id = 1
    """
    birth_date = fetch_query_one(query)[0]
    today = get_today_date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# uses fist_name for now, , modify back the retun statement
def get_gender():
    query = f"""
    SELECT first_name
    FROM users
    WHERE user_id = 1
    """
    gender = fetch_query_one(query)[0]
    return "male"

def get_weight():
    query = f"""
    SELECT weight
    FROM users
    WHERE user_id = 1
    """

    weight = fetch_query_one(query)[0]
    return weight

def get_height():
    query = f"""
    SELECT height
    FROM users
    WHERE user_id = 1
    """

    height = fetch_query_one(query)[0]
    return height
    

def get_daily_exercise_quote():
    pass

def get_daily_calories_quote():
    sex = get_gender()
    weight = get_weight()
    height = get_height()
    age = get_age()
    if sex == "John":
        BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        return BMR
    elif sex == "female":
        BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        return BMR

def get_bmi():
    weight = get_weight()
    height = get_height()/100
    bmi = weight / (height ** 2)
    return bmi





