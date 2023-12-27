import requests

ciudad = input("Ingrese una ciudad: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=bcc938b34848481d2843119f11e2b331"

res = requests.get(url)

data = res.json()

#definir 3 caracteristicas ambientales: temperatura, velocidad del viento y descripción general meterolo, lat y lonh

temp = data["main"]["temp"] #atributos main y temp porque en la data, temp es un diccionario que está dentro de otro diccionario que es main
vel_viento = data["wind"]["speed"]

latitud = data["coord"]["lat"]
longitud = data["coord"]["lon"]

descripcion = data["weather"][0]["description"] #se pone el 0 ya que description es diferente, ya que es un diccionario dentro de una lista 

print("la temperatura es: ", temp)
print("la velocidad del viento es : ", vel_viento)
print("la latitud es: ", latitud)
print("la longitud es: ", longitud)
print("la descripción es: ", descripcion)