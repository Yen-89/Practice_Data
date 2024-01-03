import datetime as dt
import requests

# Clave de la API desde las variables de entorno
api_key = "bcc938b34848481d2843119f11e2b331"

# Coordenadas de la ciudad (reemplazar con las coordenadas de la ciudad deseada)
latitud = 6.25
longitud = -75.56

# Construir la URL de la API con las coordenadas y la clave de la API
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}"
response = requests.get(url).json()

print(response)



