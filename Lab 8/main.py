import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Инициализация количества вершин
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Создание матрицы смежности

    # Нахождение вершины с минимальным расстоянием
    def minDistance(self, dist, sptSet):
        min_value = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min_value and sptSet[v] == False:
                min_value = dist[v]
                min_index = v
        return min_index

    # Вывод решения в файл
    def printSolution(self, dist):
        with open('output.txt', 'w') as file:
            file.write("Вершина \t Расстояние от начальной вершины\n")
            for node in range(self.V):
                file.write(f"{node} \t {dist[node]}\n")

    # Алгоритм Дейкстры
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V  # Инициализация массива расстояний
        dist[src] = 0  # Расстояние от начальной вершины до самой себя равно 0
        sptSet = [False] * self.V  # Массив для отслеживания посещенных вершин

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)  # Находим вершину с минимальным расстоянием
            sptSet[u] = True  # Помечаем вершину как посещенную
            for v in range(self.V):
                # Для каждой вершины, к которой можно достигнуть из текущей
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]  # Обновляем расстояние

        self.printSolution(dist)  # Выводим результат в файл

# Считываем данные из файла
with open('input.txt', 'r') as file:
    lines = file.readlines()
    vertices = int(lines[0])
    g = Graph(vertices)
    for i in range(vertices):
        values = list(map(int, lines[i+1].split()))  # Считываем значения для вершины
        for j in range(vertices):
            g.graph[i][j] = values[j]  # Заполняем матрицу смежности


source_vertex = 0
g.dijkstra(source_vertex)