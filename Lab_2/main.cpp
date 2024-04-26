#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <set>

class Graph
{
private:
    std::vector<std::vector<int>> graph;
    std::vector<std::set<int>> components;
    std::set<int> usedNodes;
    int size;
    std::map<int, std::vector<int>> distances;
    std::map<int, std::vector<int>> parents;

public:
    Graph(std::string file)
    {
        std::ifstream matrix(file);
        size = 0;
        matrix >> size;

        graph.resize(size);
        components.resize(1);
        for (int i = 0; i < size; i++)
        {
            graph[i].resize(size);
            for (int j = 0; j < size; j++)
            {
                matrix >> graph[i][j];
            }
        }
        matrix.close();

        for (int s = 0; s < size; s++)
        {
            bfs(s);
        }
    }

    void bfs(int start)
    {
        std::vector<int> d(size, 1000);
        std::vector<int> p(size, -1);
        d[start] = 0;
        std::queue<int> q;
        q.push(start);

        if ((!components.back().empty()) && usedNodes.size() != size)
        {
            components.resize(components.size() + 1);
        }

        if (!usedNodes.count(start))
        {
            components.back().insert(start);
            usedNodes.insert(start);
        }

        while (!q.empty())
        {
            int v = q.front();
            q.pop();
            if (!usedNodes.count(v))
            {
                components.back().insert(v);
                usedNodes.insert(v);
            }

            for (int i = 0; i < graph[v].size(); i++)
            {
                if (graph[v][i] != 0 && d[i] > d[v] + graph[v][i])
                {
                    p[i] = v;
                    d[i] = d[v] + graph[v][i];
                    q.push(i);
                }
            }
        }
        distances[start] = d;
        parents[start] = p;

    }

    std::vector<int> getPath(int start, int end)
    {
        std::vector<int> d = distances[start];
        std::vector<int> p = parents[start];

        if (d[end] == size)
        {
            return {};
        }

        std::vector<int> path;
        while (end != -1)
        {
            path.push_back(end);
            end = p[end];
        }

        std::reverse(path.begin(), path.end());
        return path;
    }

    int getSize()
    {
        return size;
    }

    std::vector<int> getDistance(int s)
    {
        return distances[s];
    }

    std::vector<std::set<int>> getComponents()
    {
        return components;
    }
};


int main() {
    Graph graph("C:\\Users\\GADashkov\\Desktop\\matrix.txt");
    int s = 0;

    /*for (int i = 0; i < graph.getSize(); i++)
    {
        std::vector<int> path = graph.getPath(s, i);

        for (int j = 0; j < path.size(); j++)
        {
            std::cout << path[j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;*/

    std::vector<int> d = graph.getDistance(s);

    for (int i = 0; i < d.size(); i++)
    {
        std::cout << i << " : " << d[i] << std::endl;
    }

    /*std::cout << graph.getComponents().size() << std::endl;
    for (auto comp : graph.getComponents())
    {
        for (int i : comp)
        {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }*/

    return 0;
}
