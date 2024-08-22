from initialize import make_query

# first_name VARCHAR(255) NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
# 	height SMALLINT,
# 	weight SMALLINT,
#     birth_date DATE

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



create_user()

