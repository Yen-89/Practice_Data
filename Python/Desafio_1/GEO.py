import datetime as dt
import requests

# Clave de la API desde las variables de entorno
api_key = "bcc938b34848481d2843119f11e2b331"

# Coordenadas de la ciudad
city_name = 'Medellin'
country_code = 170
limit = 5



# Construir la URL de la API con las coordenadas y la clave de la API
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={api_key}&units=metric"

response = requests.get(url).json()

print(response)