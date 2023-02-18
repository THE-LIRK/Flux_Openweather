# import requests
# import pandas as pd
# import datetime

# API_KEY ="bb5f6c27cfb755afe84c05889e78ef45"

# # Fonction pour récupérer les données météorologiques pour une ville donnée à une date donnée
# def get_historical_weather(city, date):
#     timestamp = int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&dt={timestamp}&units=metric'
#     response = requests.get(url)
#     data = response.json()
#     weather_data = {
#         'city': city,
#         'date': date,
#         'temperature':data["main"]["temp"],
#         'humidity': data['main']['humidity'],
#         'wind_speed': data['wind']['speed'],
#         "description":data["weather"][0]["description"]
#     }
#     return weather_data

# # Liste des villes et dates pour lesquelles nous souhaitons récupérer les données météorologiques
# cities = ['Paris', 'Lyon', 'Marseille']
# dates = ['2022-01-01', '2022-02-17', '2022-01-03']

# # Récupération des données météorologiques pour chaque ville et chaque date
# weather_data = []
# for city in cities:
#     for date in dates:
#         data = get_historical_weather(city, date)
#         weather_data.append(data)

# # Création du DataFrame correspondant aux données météorologiques historiques
# df = pd.DataFrame.from_dict(weather_data)
# print(df)

import requests
import pandas as pd
from datetime import datetime, timedelta

# API URL
url = "https://api.openweathermap.org/data/2.5/weather"

# API Key
api_key = "bb5f6c27cfb755afe84c05889e78ef45"

# List of cities to get data for
cities = ["Paris", "Marseille", "Lyon", "Toulouse"]

# List to store the weather data for each city
weather_data = []

# Dates range
start_date = datetime.strptime("2022-01-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
delta = timedelta(days=1)

# Loop through each city and get weather data for each day in the date range
for city in cities:
    for date in pd.date_range(start_date, end_date, freq="D"):
        # Get the weather data for the current city and date
        query_params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(url, params=query_params)
        data = response.json()
        if response.status_code == 200:
            weather_data.append({
                "city": city,
                "date": date,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            })
        else:
            print(f"Error getting weather data for {city} on {date}: {data['message']}")

# Create a pandas DataFrame from the weather data
df = pd.DataFrame(weather_data)

print(df)