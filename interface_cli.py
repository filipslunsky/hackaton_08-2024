from auxiliary_functions import get_string_input, fetch_query_one, get_today_date
from input_functions import check_email, create_user
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
    print(f"xxx")


user = User("johny.doe@gmail.com")
print(user.first_name)
print(user.last_name)
print(user.gender)
print(user.height)
print(user.weight)
print(user.birth_date)
print(user.bmi)
print(user.age)
print(user.daily_calories_quote)



