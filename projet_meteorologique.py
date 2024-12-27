# importer bibliothèque
import json
import requests
# Replace 'API_KEY' with your actual API key from NewsAPI
# num key
#API_KEY = 'c3caaa4613bf788ac4a9dd022a097bab'

# launch du programme
nbr_meteo = int(input("est ce que vous voulez entrer dans le programme?\ntapez 1 pour oui: "))
# data city

# mini dic à modifier par geolocalisation.py (fonction)
def geolocalisation_city(c_v):
    # lien API + Key
    url = f"https://api.geoapify.com/v1/geocode/search?city={c_v}&apiKey=4d64269087ff4a1ab7a804d6d3569c3a"
    # recup les infos dans le -dict.json-
    recuperer_data = requests.get(url)
    data_geoloc = recuperer_data.json()
    # afficher
    #print(data_geoloc)
    # variable lon & lat
    longitude = data_geoloc["features"][0]["properties"]["lon"]
    latitude = data_geoloc["features"][0]["properties"]["lat"]
    # add a la dict
    data_geo = {
        "longitude":longitude,
        "latitude":latitude
    }
    # retourner la liste
    return data_geo

# boucle afficher données
while nbr_meteo == 1:
    """longitude = (input("indiquer une logitude: ")
    latitude = input("indiquer une latitude : ")"""
    indiquer_ville = input("indiquer une ville: ").capitalize()
    stock_geo = geolocalisation_city(indiquer_ville)
    # url
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={stock_geo['latitude']}&lon={stock_geo['longitude']}&appid=c3caaa4613bf788ac4a9dd022a097bab"
    response = requests.get(url)
    data_data = response.json()
    print(data_data)
    stop = int(input("est ce que vous voulez continuer tapez 1, sinon tapez 2"))
    if stop != 1:
        with open("file.json", "w+") as file:
            file.write(json.dumps(data_data))
        break

# message de sortie
print("vous etes sortis du programme")

with open("file.json", "r", encoding="utf-8") as file:
    data = json.load(file)
# ---------------------_>

class Menu_data():
    def __init__(self):
        pass
    # menu
    def afficher_menu_principal(self):
        print("menu")
    for i in data:
        print(i)
    choix = input("tapez le nom de la key du menu pour acceder aux informations")


    def menu_main(c_h):
        menu_main = data[c_h][0]["description"]

