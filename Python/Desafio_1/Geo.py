import requests

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Clave de la API desde las variables de entorno
api_key = os.getenv("API_KEY")

# Verificar si la clave de la API está disponible
if not api_key:
    raise ValueError("La clave de la API no está configurada en el archivo .env")

# Coordenadas de la ciudad (reemplazar con las coordenadas de la ciudad deseada)
latitud = 6.24
longitud = -75.58

# Construir la URL de la API con las coordenadas y la clave de la API
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitud}&lon={longitud}&appid={api_key}"

# Realizar la solicitud GET a la API
res = requests.get(url)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if res.status_code == 200:
    # Convertir la respuesta JSON a un diccionario
    data = res.json()

    # Verificar si hay alertas disponibles
    alertas = data.get("alerts", [])

    if alertas:
        # Acceder a la descripción de la primera alerta
        descripcion = alertas[0]["description"]
        print("Descripción de la primera alerta:", descripcion)
    else:
        print("No hay alertas disponibles.")

else:
    # Imprimir un mensaje de error si la solicitud no fue exitosa
    print(f"Error al realizar la solicitud. Código de respuesta: {res.status_code}")
    print(res.text)
