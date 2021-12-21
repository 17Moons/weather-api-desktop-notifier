import os
import requests
import json
from pynotifier import Notification


#enter you weather api here . to get weather api you would need to make account on https://www.weatherapi.com 
#you can export the api on the server for enhanced security but here i have used it as a simple string 
weather_api_key = ""

city_name = input("Enter the city whose weather you want to know: ") 

url = (
    "https://api.weatherapi.com/v1/forecast.json?key="
    + weather_api_key
    + "&q="
    + city_name
)

response = requests.get(url)
#print(json.dumps(response.json()))

response_value = response.json()
#print(type(response_value))

location = response_value["location"]["name"]
temp = response_value["current"]["temp_c"]
condition = response_value["current"]["condition"]["text"]

notif_text = (
    "Currently in "
    + location
    + ", temprature is "
    + str(temp)
    + " degrees Celsius."
    + "\n"
    + "The condition is "
    + condition
    + "."
)

Notification(
    title="Weather news",
    description=notif_text,
    duration=10,
    urgency="normal",
).send()