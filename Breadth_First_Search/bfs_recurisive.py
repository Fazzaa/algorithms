import graph
from collections import deque

def BFS(graph, q, discovered):
    if not q:
        return
    v = q.popleft()
    print(v, end=' ')
    
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
    BFS(graph, q, discovered)

if __name__ == "__main__":
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]
    q = deque()
    n = 15
    g = graph.Graph(edges, n)
    discovered = [False]*15
    for i in range(n):
        if not discovered[i]:
            discovered[i] = True
            q.append(i)
            BFS(g, q, discovered)