import graph
from collections import deque

def BFS(graph, starting_v, discovered):
    q = deque() 
    discovered[starting_v] = True
    q.append(starting_v)

    while q:
        starting_v = q.popleft()
        print(starting_v, end=" ")
        for u in graph.adjList[starting_v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)


if __name__ == "__main__":
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]
    n = 15
    g = graph.Graph(edges, n)
    discovered = [False]*15
    for i in range(n):
        if not discovered[i]:
            BFS(g, i, discovered)