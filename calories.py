import requests
import json

def get_nutrients(food):
    api_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": "9be055c5",
        "x-app-key": "71d5e786a82fce8dda8d9c80c395f4aa",
        "Content-Type": "application/json"
    }
    try:
        query = {"query": food}

        response = requests.post(api_url, headers = headers, json = query)
        data = response.json()

        name = data['foods'][0]['food_name']
        serving_weight_grams = data['foods'][0]['serving_weight_grams']
        calories = data['foods'][0]['nf_calories']

    except KeyError:
        name = ""
        serving_weight_grams = 0
        calories = 0
    return name, serving_weight_grams, calories


def get_calories_burned(exercise_name, duration_in_minutes, height, weight, age, gender):
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    headers = {
        "x-app-id": "9be055c5",
        "x-app-key": "71d5e786a82fce8dda8d9c80c395f4aa",
        "Content-Type": "application/json"
    }

    body = {
        "query": exercise_name,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age
    }

    time_coef = duration_in_minutes / 30

    response = requests.post(url, headers=headers, json=body)
    data = response.json()


    if response.status_code == 200 and data["exercises"]:
        for exercise in data["exercises"]:
            calories_per_unit = exercise['nf_calories']
            total_calories = calories_per_unit * time_coef
            return total_calories
    else:
        return 0

print(get_calories_burned("jogging", 15, 175, 75, 38, "male"))
