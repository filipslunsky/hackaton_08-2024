Health and Food Tracker App
============

Description
-----------
The app allows user to create own profile with email and personal data, input and update body weight and height, it calculates BMI and optimal daily exercise and calorie intake. Users can log in what they ate, what exercise they did and when which is calculated into calories and they can track comparison with their personal recommended daily quota (based on BMI, age, gender etc.).
The app uses Python and PostgreSQL

Installation
------------
Instructions on how to set up the project locally.

1. Use pip to install the required modules from requirements.txt

2. Create .env file with DB access information, e.g.:
    DB_NAME = 'your_local_db_name'
    DB_USER = 'your_username'
    DB_PASSWORD = 'your_password'
    DB_HOST = 'your_host'
    DB_PORT = 'your_port'

3. Run the script from initialize to create neccessary DB tables.

4. Run the app CLI by running the script in interface_cli.py

Usage
-----
You need to input an email address to use the app that needs to be unique.
After you log in or create a new account and access your user profile, you can check your daily statistics, recommended intake of calories and daily physical activity.
You can log what food you ate and what exercise you did.
You can also update your weight and height through time and see adjusted daily goals.
