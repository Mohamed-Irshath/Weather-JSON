import requests

from pprint import pprint

API_Key = '1d255abb26fb47a927c623252d30908a'

City = input("Enter a City: ")

Base_URL = "http://api.openweathermap.org/data/2.5/weather?q="+City+"&appid="+API_Key

weather_data = requests.get(Base_URL).json()

pprint(weather_data)