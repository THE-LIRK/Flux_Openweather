import pandas as pd
import time
import requests

def get_weather_data(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    query_params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=query_params)

    return response.json()

# Remplacez "YOUR_API_KEY" par votre clé d'API OpenWeatherMap
api_key = "bb5f6c27cfb755afe84c05889e78ef45"

# Définissez les villes pour lesquelles vous souhaitez récupérer les données météorologiques
cities = ["Paris", "Lyon", "Bordeaux"]

# Initialisez une liste pour stocker les données météorologiques
weather_data = []

while True:
    # Parcourez les villes et récupérez les données météorologiques pour chaque ville
    for city in cities:
        data = get_weather_data(city, api_key)
        temp_celsius = data["main"]["temp"] - 273.15 # conversion en Celsius
        weather_dict = {
            "city": city,
            "date": pd.Timestamp.now(),
            "temp": temp_celsius,
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        weather_data.append(weather_dict)

    # Créez un DataFrame à partir des données météorologiques
    
    df= pd.DataFrame(weather_data)
    
    
    # Affichez le DataFrame en direct
    print(df)
    
    # Attendez 1 min avant de récupérer de nouvelles données
    time.sleep(60)
