import requests
import json

GENDER = 'male'
WEIGHT_KG = '88'
HEIGHT_CM = '177'
AGE = '33'

APP_ID = 'f9aefa21'
API_KEY = 'b34374083f455b0eea4d32c0a54e55a8'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheety = "https://api.sheety.co/22f8dcd631262ade7ce58b2b7145b7d1/myWorkouts/workouts"
