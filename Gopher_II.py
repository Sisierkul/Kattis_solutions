
import math
from collections import defaultdict

class Graph:

            def __init__(self, graph):
                self.graph = graph
                self. ROW = len(graph)

            def BFS(self, s, t, parent):

                visited = [False] * (self.ROW)
                queue = []

                queue.append(s)
                visited[s] = True

                while queue:

                    u = queue.pop(0)

                    for ind, val in enumerate(self.graph[u]):
                        if visited[ind] == False and val > 0:
                            queue.append(ind)
                            visited[ind] = True
                            parent[ind] = u

                return True if visited[t] else False

            def ford_fulkerson(self, source, sink):
                parent = [-1] * (self.ROW)
                max_flow = 0

                while self.BFS(source, sink, parent):

                    path_flow = float("Inf")
                    s = sink
                    while(s != source):
                        path_flow = min(path_flow, self.graph[parent[s]][s])
                        s = parent[s]

                    max_flow += path_flow

                    v = sink
                    while(v != source):
                        u = parent[v]
                        self.graph[u][v] -= path_flow
                        self.graph[v][u] += path_flow
                        v = parent[v]

                return max_flow

try:
    while True:
        n, m, s, v = map(int, input().split())

        gopher_xs = [0]
        gopher_ys = [0]
        hole_xs = [0]
        hole_ys = [0]
        maxdist = s*v*10
        matchings = []

        for _ in range (n):
            x, y = [int(float(x)*10) for x in input().split()]
            gopher_xs.append(x)
            gopher_ys.append(y)
        for _ in range (m):
            x, y = [int(float(x)*10) for x in input().split()]
            hole_xs.append(x)
            hole_ys.append(y)

        def getDist(x1, y1, x2, y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)

        G = [[0 for _ in range (n+m+2)] for _ in range (n+m+2)]

        for i in range (1,n+1):
            G[0][i] = 1
            for j in range(1,m+1):
                if getDist(gopher_xs[i], gopher_ys[i], hole_xs[j], hole_ys[j]) <= maxdist:
                    G[i][j+n] = 1
        for j in range(n+1,n+m+1):
            G[j][-1] = 1
            
        bipG = Graph(G)

        s = 0
        t = n+m+1

        print(n-bipG.ford_fulkerson(s,t))
except EOFError:
    pass
