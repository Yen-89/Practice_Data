import requests

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Clave de la API desde las variables de entorno
api_key = os.getenv("API_KEY")


# Coordenadas de la ciudad (reemplazar con las coordenadas de la ciudad deseada)
latitud = 6.2518
longitud = -75.5636

# Construir la URL de la API con las coordenadas y la clave de la API
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}.34&lon={longitud}&appid={api_key}"

# Realizar la solicitud GET a la API
res = requests.get(url)
print("---------------------------")
print("---------------------------")

print(res)

print("---------------------------")

print("---------------------------")


