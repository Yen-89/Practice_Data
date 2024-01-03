import datetime as dt
import requests

##BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "bcc938b34848481d2843119f11e2b331"
CITY = input("Enter a city: ")

##url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

##print(response)

lon = response['coord']['lon']
lat = response['coord']['lat']
temp = response['main']['temp']
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
descript = response ['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Longitude in {CITY} is: {lon}")
print(f"Latitude in {CITY} is: {lat}") 
print(f"Temperature in {CITY} is: {temp}°C") 
print(f"Humidity in {CITY} is: {humidity}%")
print(f"Wind Speed in {CITY} is: {wind_speed}m/s")
print(f"General Wather in {CITY} is: {descript}")
print(f"Sun rises in {CITY} is: at {sunrise_time} at local time")
print(f"Sun sets in {CITY} is: at {sunset_time} at local time")