# Функция для чтения графа из файла
def read_graph(file_name):
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline().strip())
        graph = []
        for _ in range(num_vertices):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)
    return graph

# Функция для нахождения эйлерова цикла в графе
def find_eulerian_cycle(graph):
    num_vertices = len(graph)
    degree = [sum(row) for row in graph]  # Считаем степень каждой вершины
    for d in degree:
        if d % 2 != 0:
            return None  # Если степень вершины нечетная, то эйлеров цикл не существует
    stack = [0]
    cycle = []
    while stack:
        v = stack[-1]  # Берем вершину с вершины стека
        if any(graph[v]):  # Если есть неиспользованные ребра
            u = next(i for i, x in enumerate(graph[v]) if x)  # Находим такую вершину u, что v связана с u
            stack.append(u)  # Добавляем эту вершину в стек
            graph[v][u] -= 1  # Удаляем ребро v-u из графа
            graph[u][v] -= 1  # Удаляем ребро u-v из графа, т.к. граф неориентированный
        else:
            cycle.append(stack.pop())  # Если из вершины v не осталось ребер, добавляем ее в цикл и убираем из стека
    return cycle[::-1]  # Возвращаем цикл в правильном порядке


file_name = 'input.txt'
graph = read_graph(file_name)
eulerian_cycle = find_eulerian_cycle(graph)


output_file = 'output.txt'
with open(output_file, 'w') as file:
    if eulerian_cycle:
        file.write('Eulerian cycle found:\n')
        file.write(' -> '.join(map(str, eulerian_cycle))) 
    else:
        file.write('Graph does not have an Eulerian cycle.')
