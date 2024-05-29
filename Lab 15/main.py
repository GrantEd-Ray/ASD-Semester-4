from typing import List 

def read_adjacency_matrix(file_path: str) -> List[List[int]]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        adjacency_matrix = [[0] * n for _ in range(n)]
        for i in range(1, n + 1):
            row = [int(x) for x in lines[i].split()]
            for j in range(n):
                adjacency_matrix[i - 1][j] = row[j]

        return adjacency_matrix


def graph_coloring(adjacency_matrix: List[List[int]]) -> List[int]:
    n = len(adjacency_matrix)
    colors = [0] * n  # Создаем список для хранения цветов вершин, изначально заполненный нулями

    def is_safe(v, c):  # Функция для проверки, можно ли назначить цвет c вершине v
        for i in range(n):  # Проходимся по всем вершинам графа
            if adjacency_matrix[v][i] == 1 and c == colors[i]:  # Если вершина v смежна с вершиной i и цвет c уже назначен вершине i
                return False
        return True  # Возвращаем True, если цвет c можно назначить вершине v

    def color_util(v, color):  # Рекурсивная функция для раскраски графа
        if v == n:  # Если все вершины раскрашены
            return True  # Возвращаем True, так как найдено допустимое решение

        for c in range(1, color + 1):  # Проходимся по всем доступным цветам
            if is_safe(v, c):  # Если цвет c можно назначить вершине v, назначаем цвет c вершине v
                colors[v] = c 
                if color_util(v + 1, color):
                    return True
                colors[v] = 0  # Если не удалось найти решение, сбрасываем цвет вершины v

        return False  # Если не удалось раскрасить граф с текущим количеством цветов, возвращаем False

    color = 1
    while not color_util(0, color):  # Пока не найдено допустимое решение
        color += 1  # Увеличиваем количество цветов

    return colors


def main():
    file_path = 'input.txt'
    adjacency_matrix = read_adjacency_matrix(file_path)

    colors = graph_coloring(adjacency_matrix)
    print(f"Минимальное количество цветов: {max(colors)}")
    print("Цвета вершин:")
    for i in range(len(adjacency_matrix)):
        print(f"Вершина {i} -> Цвет {colors[i]}")

if __name__ == "__main__":
    main()
