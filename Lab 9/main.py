def read_graph(file_name):
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline().strip())
        graph = []
        for _ in range(num_vertices):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)
    return graph

def bellman_ford(graph, source):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices  # Инициализация массива расстояний
    distances[source] = 0  # Расстояние от начальной вершины до нее самой равно 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                if graph[u][v] != 0:  # Проверка наличия ребра между вершинами u и v
                    if distances[u] + graph[u][v] < distances[v]:
                        distances[v] = distances[u] + graph[u][v]  # Обновление расстояния

    return distances

file_name = 'input.txt'
source_vertex = 0

graph = read_graph(file_name)
shortest_distances = bellman_ford(graph, source_vertex)

output_file = 'output.txt'
with open(output_file, 'w') as file:
    for vertex, distance in enumerate(shortest_distances):
        file.write(f'Расстояние от вершины {source_vertex} до вершины {vertex}: {distance}\n')
