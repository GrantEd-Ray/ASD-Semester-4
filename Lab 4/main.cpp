#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

const int MAX_N = 1000; // Предполагаем, что максимальное количество вершин не превышает 1000
vector<int> graph[MAX_N]; // Список смежности для хранения графа
bool visited[MAX_N]; // Массив для отслеживания посещенных вершин
vector<int> component; // Вектор для хранения текущей компоненты связности

// Функция для рекурсивного поиска в глубину
void dfs(int v) {
    visited[v] = true; // Помечаем вершину как посещенную
    component.push_back(v); // Добавляем вершину в текущую компоненту связности

    for (int u : graph[v]) { // Перебираем всех соседей вершины v
        if (!visited[u]) {
            dfs(u); // Рекурсивно посещаем каждого не посещенного соседа
        }
    }
}

int main() {
    ifstream fin("input.txt"); // Открытие файла для чтения
    ofstream fout("output.txt"); // Открытие файла для записи результатов

    int n; // Количество вершин в графе
    fin >> n; // Считываем количество вершин

    // Считываем матрицу смежности и строим список смежности
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int edge;
            fin >> edge;
            if (edge == 1) { // Если между вершинами i и j есть ребро
                graph[i].push_back(j);
            }
        }
    }

    int componentsCount = 0; // Счетчик компонент связности
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i); // Запускаем поиск в глубину из вершины i
            componentsCount++; // Увеличиваем счетчик компонент связности

            // Записываем состав текущей компоненты связности в файл
            fout << "Компонента связности " << componentsCount << ": ";
            for (int v : component) {
                fout << v << " ";
            }
            fout << endl;

            component.clear(); // Очищаем вектор для следующей компоненты связности
        }
    }
    fout << "Всего компонент связности: " << componentsCount;
    // Закрытие файлов
    fin.close();
    fout.close();

    return 0;
}