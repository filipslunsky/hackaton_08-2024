from auxiliary_functions import get_string_input, get_email_input, get_today_date, get_date_input
from input_output_func import check_email, create_user, log_exercise, log_food_intake, get_exercise_info, get_food_info, update_user_info
from calculations_user import User

def display_entry_menu():
    print("""
-----------------------------
| WELCOME TO HEALTH TRACKER |
-----------------------------
          """)
    choice = get_string_input("""
Do you want to (l)og in to your existing account?
Or (c)reate a new account and get healthier every day?
""", ["l", "c"])
    email = get_email_input("What is your email, please?  ")
    if choice == "c":
        while True:
            if check_email(email):
                email = input("This email is already registered, enter another one, please:  ")
            else:
                break
        create_user(email)
        display_main_menu(email)
    elif choice == "l":
        while True:
            if not check_email(email):
                email = input("This email is not in our database, try again:  ")
            else:
                break
        display_main_menu(email)


def display_main_menu(email):
    user = User(email)
    choice = get_string_input(f"""
Good to see you, {user.first_name}                                  
What would you like to do?
  -- log new (e)xercise you did --
  -- log new (f)ood you ate     -- 
  --------------------------------
  -- change your user (i)nfo    -- 
  -- see your (s)tatistics      --        
  ----------- (q)uit -------------                                 
                                                  
""", ["e", "f", "i", "s", "q"])
    
    if choice == "e":
        log_exercise(email)
        print("exercise logged")
        display_main_menu(email)
    elif choice == "f":
        log_food_intake(email)
        print("food logged")
        display_main_menu(email)
    elif choice == "i":
        update_user_info(email)
        print("settings changed")
        choice = get_string_input("Back to (m)ain menu or (q)uit?  ", ["m", "q"])
        if choice == "m":
            display_main_menu(email)
        elif choice == "q":
            print(f"Have a great day, {user.first_name}, come back soon.")
    elif choice == "s":
        date = get_today_date()
        display_stats(email, user.age, user.weight, user.height, user.bmi, user.daily_calories_quote, user.daily_exercise_quote, date)
        while True:
            choice = get_string_input("Back to (m)ain menu, see (d)ifferent day or (q)uit?  ", ["m", "q", "d"])
            if choice == "m":
                display_main_menu(email)
                break
            elif choice == "d":
                date = get_date_input()
                display_stats(email, user.age, user.weight, user.height, user.bmi, user.daily_calories_quote, user.daily_exercise_quote, date)
                choice = "m"
            elif choice == "q":
                print(f"Have a great day, {user.first_name}, come back soon.")
                break
    elif choice == "q":
        print(f"Have a great day, {user.first_name}, come back soon.")


def display_stats(email, age, weight, height, bmi, daily_calories_quote, daily_exercise_quote, date):
    food_results = get_food_info(email, date)
    exercise_info = get_exercise_info(email, date)
    remaining_food = daily_calories_quote - food_results[1]
    remaining_exercise = daily_exercise_quote - exercise_info[2]
    print(f"""
FOOD INTAKE:            {round(food_results[1], 2)} Kcal ( in form of {food_results[0]})
OPTIMAL DAILY INTAKE:   {round(daily_calories_quote, 2)} Kcal
REMAINING INTAKE:       {round(remaining_food, 2)} Kcal
PHYSICAL ACTIVITY:      {round(exercise_info[2], 2)} cal ( by doing {exercise_info[0]} for total of {exercise_info[1]} minutes )
DAILY GOAL:             {round(daily_exercise_quote, 2)} cal
REMAINING EXERCISE:     {round(remaining_exercise, 2)} cal
------------------------------------------------------------------------------------
AGE:                    {age} years old
BODY WEIGHT:            {weight} kg
HEIGHT:                 {height} cm
Body Mass Index:        {round(bmi, 2)}
------------------------------------------------------------------------------------
DATE:                   {date}

""")    


display_entry_menu()