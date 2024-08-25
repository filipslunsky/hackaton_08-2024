from auxiliary_functions import get_string_input, fetch_query_one, get_today_date
from input_functions import check_email, create_user, log_exercise, log_food_intake, get_exercise_info, get_food_info
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
    email = input("Cool, what is your email please?  ")
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
        print("settings changed")
        choice = get_string_input("Back to (m)ain menu or (q)uit?  ", ["m", "q"])
        if choice == "m":
            display_main_menu(email)
        elif choice == "q":
            print(f"Have a great day, {user.first_name}, come back soon.")
    elif choice == "s":
        food_results = get_food_info(email)
        exercise_info = get_exercise_info(email)
        remaining_food = user.daily_calories_quote - food_results[1]
        remaining_exercise = user.daily_exercise_quote - exercise_info[2]
        print(f"""
FOOD INTAKE:            {food_results[1]} Kcal (in form of {food_results[0]})
OPTIMAL DAILY INTAKE:   {user.daily_calories_quote} Kcal
REMAINING INTAKE:       {remaining_food}
PHYSICAL ACTIVITY:      {exercise_info[2]} cal (by doing {exercise_info[0]} for total of {exercise_info[1]} minutes)
DAILY GOAL:             {user.daily_exercise_quote} cal
REMAINING EXERCISE:     {remaining_exercise}
----------------------------------------------------------------------------------------------
AGE:                    {user.age}
BODY WEIGHT:            {user.weight} kg
HEIGHT:                 {user.height} cm
Body Mass Index:        {user.bmi}

""")
        choice = get_string_input("Back to (m)ain menu or (q)uit?  ", ["m", "q"])
        if choice == "m":
            display_main_menu(email)
        elif choice == "q":
            print(f"Have a great day, {user.first_name}, come back soon.")
    elif choice == "q":
        print(f"Have a great day, {user.first_name}, come back soon.")


display_entry_menu()