import os
import pickle
import osmnx as ox

ox.settings.use_cache = True

def get_coordinate(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_latitude(prompt):
    while True:
        latitude = get_coordinate(prompt)
        if -90 <= latitude <= 90:
            return latitude
        else:
            print("Latitude must be between -90 and 90 degrees.")

def get_longitude(prompt):
    while True:
        longitude = get_coordinate(prompt)
        if -180 <= longitude <= 180:
            return longitude
        else:
            print("Longitude must be between -180 and 180 degrees.")

def load_or_download_graph(country, city, network_type):
    filename = f"loaded_maps/{city.lower()}_{network_type}.pkl"

    # Проверка, существует ли файл
    if os.path.exists(filename):
        print("Загружаем граф из файла...")
        with open(filename, "rb") as f:
            return pickle.load(f)
    else:
        print("Скачиваем и сохраняем граф...")
        G = ox.graph_from_place(f"{country}, {city}", network_type=network_type)
        os.makedirs("modules/cache", exist_ok=True)
        with open(filename, "wb") as f:
            pickle.dump(G, f)
        return G
