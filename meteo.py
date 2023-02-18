import requests
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)




# Titre du tableau
st.title("Real-Time / Live Data Science Dashboard")

# Définir les villes pour lesquelles vous voulez obtenir les informations météo
# cities = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne", "Saint-Denis", "Le Mans", "Aix-en-Provence", "Clermont-Ferrand", "Brest", "Tours", "Limoges", "Amiens", "Annecy", "Perpignan", "Boulogne-Billancourt", "Metz", "Besançon", "Orléans", "Saint-Denis", "Argenteuil", "Mulhouse", "Rouen", "Montreuil", "Caen", "Nancy", "Saint-Paul", "Tourcoing", "Nanterre", "Avignon", "Vitry-sur-Seine", "Créteil", "Poitiers", "Dunkerque", "Aubervilliers", "Versailles", "Aulnay-sous-Bois", "Asnières-sur-Seine", "Colmar", "Courbevoie", "Saint-Pierre", "Saint-Maur-des-Fossés", "Cherbourg-en-Cotentin", "Rueil-Malmaison", "Pau", "La Rochelle", "Calais", "Champigny-sur-Marne", "Saint-Nazaire", "Béziers", "Vénissieux", "Villejuif", "Cholet", "Saint-Quentin", "Colombes", "Quimper", "Issy-les-Moulineaux", "Noisy-le-Grand", "Sarcelles", "Les Abymes", "Le Tampon", "Vannes", "Fréjus", "Arles", "La Seyne-sur-Mer", "Maisons-Alfort", "Cagnes-sur-Mer", "Montauban", "Neuilly-sur-Seine", "Choisy-le-Roi", "Haguenau", "Plaisir", "Laval", "Évreux", "Sète", "Châtillon", "Livry-Gargan", "Vincennes", "Alès", "L'Haÿ-les-Roses", "Agen", "Villeneuve-Saint-Georges", "Lunel", "Vierzon"]
cities = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims"]

# Définir votre clé API
api_key = "bb5f6c27cfb755afe84c05889e78ef45"

# Initialiser le dictionnaire qui stockera les données de chaque ville
weather_data = {"city": [], "temperature": [], "humidity": [], "wind_speed": [], "description": [],}

# Boucle sur chaque ville pour interroger l'API et stocker les données dans le dictionnaire
for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
      
    weather_data["city"].append(city)
    weather_data["temperature"].append(data["main"]["temp"]- 273.15)
    weather_data["humidity"].append(data["main"]["humidity"])
    weather_data["wind_speed"].append(data["wind"]["speed"])
    weather_data["description"].append(data["weather"][0]["description"])

# Créer un DataFrame à partir du dictionnaire
df = pd.DataFrame(weather_data)


# top-level filters
your_city = st.selectbox("select the city", pd.unique(df["city"]))
# dataframe filter
df = df[df["city"] == your_city]

# create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="TEMPERATURE ° 🌡️",
    value=int(df["temperature"])
)



kpi2.metric(
    label="HUMIDITY %💧",
    value= int(df["humidity"])
    
)


kpi3.metric(
    label="WIND_SPEED m/s💨",
    value=int(df["wind_speed"])
    
)


st.dataframe(df)









# kpi2.metric(
#     label="Married Count 💍",
#     value=int()),
#     delta=,
# )

# kpi3.metric(
#     label="A/C Balance ＄",
#     value=f"$ {round(balance,2)} ",
#     delta=-round(balance / count_married) * 100,
# )

