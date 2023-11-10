def fuckme(a,b):
    return a*2*b

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        #supposing it is a undirected graph
        for(src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
