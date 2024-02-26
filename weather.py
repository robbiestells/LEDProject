import requests
import datetime
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time

key = '030f9dc6ee174caeb79211946242301'
currentUri = 'http://api.weatherapi.com/v1/forecast.json?key='  + key + '&q=06109&days=5&aqi=no&alerts=no'

def GetForecast():

    resp = requests.get(url=currentUri)
    data = resp.json()
    temp = str(round(data["current"]["temp_f"])) + "F"
    condition = data["current"]["condition"]["text"]
    print("Currently: " + temp + ", " + condition)

    forecast = data["forecast"]["forecastday"]
    #print(forecast)
    for day in forecast:
        # Convert the string to a datetime object
        date_object = datetime.datetime.strptime(day["date"], '%Y-%m-%d')

        # Get the day of the week
        day_of_week = date_object.strftime('%A')
        #print(day_of_week)

        # Get the temp
        dayTemp = str(round(day["day"]["maxtemp_f"])) + "F"
        #print(dayTemp)

        # Get the condition
        dayCondition = day["day"]["condition"]["text"]
        #print(dayCondition)
        print(day_of_week + ": " + dayTemp + ", " + dayCondition)
    return dayTemp
#needs to return all days

def GetCurrentWeather():
    resp = requests.get(url=currentUri)
    data = resp.json()
    temp = str(round(data["current"]["temp_f"])) + "F"
    condition = data["current"]["condition"]["text"]
    print("Currently: " + temp + ", " + condition)
    conditionImage = data["current"]["condition"]["icon"]
    return [temp, condition, conditionImage]

