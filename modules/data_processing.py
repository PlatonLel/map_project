import osmnx as ox
from geopy.distance import geodesic
import networkx as nx


def get_small_subgraph(Graph, lat1, lon1, lat2, lon2, min_radius=0, max_radius=0, step=0):
    # Определение ближайших узлов
    source_node = ox.distance.nearest_nodes(Graph, lon1, lat1)
    target_node = ox.distance.nearest_nodes(Graph, lon2, lat2)

    coord1 = (lon1, lat1)
    coord2 = (lon2, lat2)

    if not (min_radius and max_radius and step):
        min_radius = geodesic(coord1, coord2).meters + 100
        max_radius = min_radius * 1.5
        step = (max_radius - min_radius) / 7

    radius = min_radius
    while radius < max_radius:
        subgraph_main = nx.compose(nx.ego_graph(Graph, source_node, radius, distance="length"),
                                   nx.ego_graph(Graph, target_node, radius, distance="length"))

        if target_node in subgraph_main:
            return subgraph_main, source_node, target_node
        radius += step

    raise ValueError(f"Не удалось соединить точки в радиусе до {max_radius} метров.")


def find_shortest_path(Graph, source, target):
    # Поиск кратчайшего пути
    return nx.shortest_path(Graph, source=source, target=target, weight="length")
