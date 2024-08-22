import requests
import json

calories_api = requests.get("https://api.api-ninjas.com/v1/nutrition")

data = calories_api.json()

file_name = 'first_food.json'
with open(file_name, 'w') as file:
    json.dump(data[0], file, indent = 2)