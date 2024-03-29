#include <iostream>
#include <fstream>
#include <vector>
#include <queue>


int main() {
    std::ifstream matrix("C:\\CLionProjects\\ASD_Lab_2_3\\matrix.txt");

    int n;
    matrix >> n;

    std::vector<std::vector<int>> g(n);
    for (int i = 0; i < n; i++)
    {
        g[i].resize(n);
        for (int j = 0; j < n; j++)
        {

            matrix >> g[i][j];
        }
    }
    matrix.close();

    int s = 0;

    std::queue<int> q;
    q.push(s);
    std::vector<int> lengths(n, -1);
    std::vector<int> parents(n, -1);
    lengths[s] = 0;

    while (!q.empty())
    {
        int v = q.front();
        q.pop();

        for (int i = 0; i < g[v].size(); ++i)
        {
            int to = g[v][i];
            if (lengths[to] == -1)
            {
                q.push(to);
                lengths[to] = lengths[v] + 1;
                parents[to] = v;
                q.push(to);
            }

        }
    }

    for (int i = 0; i < parents.size(); i++)
    {
        std::cout << i << '(' << lengths[i] << ")\t:";
        int x = parents[i];
        while (x != -1)
        {
            std::cout << x << ' ';
            x = parents[x];
        }
        std::cout << std::endl;
    }

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
