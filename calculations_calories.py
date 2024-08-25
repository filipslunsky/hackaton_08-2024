import requests
from auxiliary_functions import get_number_input

def get_calories_burned(exercise_name, duration_in_minutes, height, weight, age, gender):
    '''function uses free version of API and returns number of burned calories'''
    # public API with a free key and ID
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
    # since the API is free, it provides the calories info for 30 minutes and ignores the time parameter, the time_coef compensates for this
    time_coef = duration_in_minutes / 30

    response = requests.post(url, headers=headers, json=body)
    data = response.json()


    if response.status_code == 200 and data["exercises"]:
        for exercise in data["exercises"]:
            calories_per_unit = exercise["nf_calories"]
            total_calories = calories_per_unit * time_coef
            return total_calories
    else:
        return 0

def get_nutrients(food):
    '''function uses free version of API and returns tuple (food, grams, calories)'''
    # public API with a free key and ID
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

        name = data["foods"][0]["food_name"]
        serving_weight_grams = data["foods"][0]["serving_weight_grams"]
        calories = data["foods"][0]["nf_calories"]

    except KeyError:
        name = ""
        serving_weight_grams = 0
        calories = 0
    
    return name, serving_weight_grams, calories


def get_calories_for_food(string):
    ''''function parses user input of food'''
    # cleaning the input from separating characters and making a list of keywords
    string = string.replace(",", "")
    string = string.replace("."," ")
    food_list = string.split(" ")

    # trying the keywords and their pairs in the API and stroring unempty results
    results = []
    for i in range(4):
        sublist = food_list[0 + i : 2 + i]
        food = " ".join(sublist)
        result = get_nutrients(food)
        if result[0] != "":
            results.append(result)
    
    # filtering out duplicate results and less accurate results (e.g. results for "chicken" are less accourate than results for "fried chicken")
    food_list = list(set(results))
    food_list.sort(key=lambda x: len(x[0]), reverse=True)
    filtered_list = []
    for item in food_list:
        if not any(item[0] in other[0] for other in filtered_list):
            filtered_list.append(item)
    
    return filtered_list


def calculate_total_calories(list_of_tuples_food):
    '''function orders consumed food and calories in a dictionary'''
    food_intake = {}
    for item in list_of_tuples_food:
        quantity = get_number_input(f"How many grams of {item[0]} did you eat?  ")
        calories = (item[2] / item[1]) * quantity
        food_intake[item[0]] = calories
    
    return food_intake

if __name__ == "__main__":
    print(get_calories_burned("squats", 15, 175, 75, 30, "male"))
    calories = get_calories_for_food("boiled chicken with rice")
    print(calories)
    print(calculate_total_calories(calories))


