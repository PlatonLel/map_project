from modules.data_load import *
from modules.data_processing import get_small_subgraph, find_shortest_path

# Ввод данных
country = input("Введите страну: \n")
city = input("Введите город: \n")

network_types = {
    '1': 'all',
    '2': 'all_public',
    '3': 'bike',
    '4': 'drive',
    '5': 'drive_service',
    '6': 'walk'
}

print("Choose the type of map:")
for key, value in network_types.items():
    print(f"{key}: {value}")

user_input = input("Enter the number corresponding to the type of map: ")
network_type = network_types.get(user_input)

if not network_type:
    print("Invalid input. Exiting...")
    exit()

# Загрузка графа
Graph = load_or_download_graph(country, city, network_type)

# Ввод координат
print("Enter coordinates for the first point:")
lat1 = get_latitude("Enter latitude (between -90 and 90): ")
lon1 = get_longitude("Enter longitude (between -180 and 180): ")

print("Enter coordinates for the second point:")
lat2 = get_latitude("Enter latitude (between -90 and 90): ")
lon2 = get_longitude("Enter longitude (between -180 and 180): ")

# Обработка данных
subgraph_main, source_node, target_node = get_small_subgraph(Graph, lat1, lon1, lat2, lon2)
shortest_path = find_shortest_path(subgraph_main, source_node, target_node)

print(f"Shortest path: {shortest_path}")
