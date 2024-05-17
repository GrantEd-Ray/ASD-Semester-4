# Находит множество вершины i
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


# Объединяет вершины i и j. Возвращает False, если i и j уже находятся в одном множестве.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b


# Находит минимальное остовное дерево с помощью алгоритма Краскала
def kruskalMST(cost):
    mincost = 0  # Стоимость минимального остовного дерева

    # Инициализация наборов непересекающихся множеств
    for i in range(V):
        parent[i] = i

    # Создание списка ребер для сортировки
    edges = []
    for i in range(V):
        for j in range(i + 1, V):
            if cost[i][j] != 0:
                edges.append((i, j, cost[i][j]))

    # Сортировка ребер по их весу
    edges.sort(key=lambda x: x[2])

    # Включаем минимальные ребра по одному
    edge_count = 0
    with open('output.txt', 'w') as f:
        for edge in edges:
            a, b, weight = edge
            if find(a) != find(b):  # Проверяем, находятся ли вершины a и b в одном и том же множестве.
                union(a, b)
                f.write(f'{a} - {b}    cost: {weight}\n')
                mincost += weight
                edge_count += 1
                if edge_count == V - 1:
                    break

        f.write(f"Minimum cost = {mincost}\n")


# Чтение графа из файла
with open('input.txt', 'r') as file:
    V = int(file.readline().strip())
    cost = [[int(x) for x in line.split()] for line in file]

parent = [i for i in range(V)]
kruskalMST(cost)