import requests

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Clave de la API desde las variables de entorno
api_key = os.getenv("API_KEY")

# Usar la variable api_key para realizar la consulta a la API

ciudad = input("Ingrese una ciudad: ")

url = f"http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=5&appid={api_key}"

res = requests.get(url)

data = res.json()

#definir 3 caracteristicas ambientales: temperatura, velocidad del viento y descripción general meterolo, lat y lonh

#temp = data["main"]["temp"] #atributos main y temp porque en la data, temp es un diccionario que está dentro de otro diccionario que es main
#vel_viento = data["wind"]["speed"]

latitud = data["lat"]["lat"]
longitud = data["lon"]["lon"]

#descripcion = data["weather"][0]["description"] #se pone el 0 ya que description es diferente, ya que es un diccionario dentro de una lista 

#print("la temperatura es: ", temp)
#print("la velocidad del viento es : ", vel_viento)
print("la latitud es: ", latitud)
print("la longitud es: ", longitud)
#print("la descripción es: ", descripcion)