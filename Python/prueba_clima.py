import requests
from datetime import datetime

# Configuración
ciudad = "Bucaramanga"
clave_api = "bcc938b34848481d2843119f11e2b331"

# Obtener información del pronóstico (forecast)
url_forecast = f"http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={clave_api}"
respuesta_forecast = requests.get(url_forecast)
datos_forecast = respuesta_forecast.json()

# Obtener información de la polución
url_polucion = f"http://api.openweathermap.org/data/2.5/air_pollution?q={ciudad}&appid={clave_api}"
respuesta_polucion = requests.get(url_polucion)
datos_polucion = respuesta_polucion.json()

# Obtener información de alarmas gubernamentales (si está disponible)
url_alarmas = f"http://api.openweathermap.org/data/2.5/onecall?lat=LATITUD&lon=LONGITUD&exclude=hourly,minutely,daily&appid={clave_api}"
# Reemplaza LATITUD y LONGITUD con las coordenadas de la ciudad (puedes obtenerlas de la respuesta del pronóstico)
respuesta_alarmas = requests.get(url_alarmas)
datos_alarmas = respuesta_alarmas.json()

# Procesar la información según tus necesidades
# ...

# Puedes imprimir los datos para ver la estructura
print("Datos del Pronóstico:", datos_forecast)
print("Datos de Polución:", datos_polucion)
print("Datos de Alarmas Gubernamentales:", datos_alarmas)
