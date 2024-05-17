INF = 9999999

# Чтение матрицы смежности из файла
with open("input.txt", "r") as file:
    V = int(file.readline().strip())
    G = [list(map(int, line.split())) for line in file]

selected = [0] * V  # Список для отслеживания выбранных вершин
selected[0] = True
no_edge = 0  # Счетчик ребер
total_weight = 0  # Общий вес минимального остовного дерева

output_file = open("output.txt", "w")

output_file.write("Edge : Weight\n")

# Поиск минимального остовного дерева
# Пока количество выбранных ребер меньше, чем число вершин минус один (так как в минимальном остовном дереве должно быть V-1 ребро)
while no_edge < V - 1:
    minimum = INF 
    x = 0  # Инициализируем переменные для хранения вершин ребра
    y = 0
    # Перебираем все вершины
    for i in range(V):
        if selected[i]:  # Если вершина i уже выбрана
            for j in range(V):
                # Если вершина j не выбрана и между вершинами i и j есть ребро
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]  # Обновляем минимальное значение и вершины ребра
                        x = i
                        y = j
    output_file.write(str(x) + "-" + str(y) + "  :   " + str(G[x][y]) + "\n")  # Записываем выбранное ребро в файл
    total_weight += G[x][y]  # Увеличиваем общий вес на вес выбранного ребра
    selected[y] = True  # Помечаем вершину y как выбранную
    no_edge += 1  # Увеличиваем счетчик выбранных ребер

output_file.write(f"\nTotal weight of minimum spanning tree: {total_weight}")

output_file.close()