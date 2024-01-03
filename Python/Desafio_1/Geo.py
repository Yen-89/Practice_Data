import datetime as dt
import requests

# Clave de la API desde las variables de entorno
api_key = "bcc938b34848481d2843119f11e2b331"

# Coordenadas de la ciudad (reemplazar con las coordenadas de la ciudad deseada)
latitud = 6.25
longitud = -75.56

# Construir la URL de la API con las coordenadas y la clave de la API
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}&units=metric"
response = requests.get(url).json()

##print(response)

lon = response['coord']['lon']
lat = response['coord']['lat']
temp = response['main']['temp']
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
descript = response ['weather'][0]['description']
name_city = response['name'] 
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Longitude is: {lon}")
print(f"Latitude is: {lat}") 
print(f"Temperature is: {temp}°C") 
print(f"Humidity in is: {humidity}%")
print(f"Wind Speed is: {wind_speed}m/s")
print(f"General Wather is: {descript}")
print(f"Name the city is: {name_city}")
print(f"Sun rises is: at {sunrise_time} at local time")
print(f"Sun sets is: at {sunset_time} at local time")




