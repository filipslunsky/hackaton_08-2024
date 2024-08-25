from auxiliary_functions import fetch_query_one, get_today_date

def get_user_id(email):
    query = f"""
    SELECT user_id
    FROM users
    WHERE email = '{email}'
    """
    email = fetch_query_one(query)[0]
    return email

user_id = get_user_id("johny.doe@gmail.com") # for testing purposes only

def get_age(user_id):
    query = f"""
    SELECT birth_date
    FROM users
    WHERE user_id = '{user_id}'
    """
    
    birth_date = fetch_query_one(query)[0]
    today = get_today_date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_gender(user_id):
    query = f"""
    SELECT gender
    FROM users
    WHERE user_id = '{user_id}'
    """
    gender = fetch_query_one(query)[0]
    return gender

def get_weight(user_id):
    query = f"""
    SELECT weight
    FROM users
    WHERE user_id = '{user_id}'
    """

    weight = fetch_query_one(query)[0]
    return weight

def get_height(user_id):
    query = f"""
    SELECT height
    FROM users
    WHERE user_id = '{user_id}'
    """

    height = fetch_query_one(query)[0]
    return height
    

def get_daily_calories_quote():
    gender = get_gender(user_id)
    weight = get_weight(user_id)
    height = get_height(user_id)
    age = get_age(user_id)
    if gender == "male":
        BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        return BMR
    elif gender == "female":
        BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        return BMR

def get_bmi():
    weight = get_weight(user_id)
    height = get_height(user_id)/100
    bmi = weight / (height ** 2)
    return bmi

class User:
    def __init__(self, email):
        self.email = email
        query = f"SELECT * FROM users WHERE email = '{self.email}'"
        result = fetch_query_one(query)
        self.first_name = result[2]
        self.last_name = result[3]
        self.gender = result[4]
        self.height = result[5]
        self.weight = result[6]
        self.birth_date = result[7]
    
    @property
    def bmi(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi
    
    @property
    def age(self):
        today = get_today_date()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    @property
    def daily_calories_quote(self):
        if self.gender == "male":
            BMR = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
            return BMR
        elif self.gender == "female":
            BMR = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
            return BMR
    
    @property
    def daily_exercise_quote(self):
        if self.bmi < 20:
            return 400
        elif self.bmi >= 20 and self.bmi < 25:
            return 500
        elif self.bmi >= 25 and self.bmi < 30:
            return 650
        else:
            return 750





