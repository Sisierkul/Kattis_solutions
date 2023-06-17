n, m, p = map(int, input().split())

G = [[0 for _ in range(n+m+p+2)]for _ in range (n+m+p+2)]

for i in range (1, n+1):
    G[0][i] = 1
    connections = input().split()
    for j in range(1, len(connections)):
        G[i][n+int(connections[j])] = 1

connected = []

for i in range (n+m+1, n+m+p+1):
    toyLimits = list(map(int, input().split()))
    for j in range(1, len(toyLimits)-1):
        connected.append(n+toyLimits[j])
        G[n+toyLimits[j]][i] = 1
    G[i][-1] = toyLimits[-1]

for x in range(n+1, n+m+1):
    if x not in connected:
        G[x][-1] = 1

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
    
bipG = Graph(G)

s = 0
t = n+m+p+1

print(bipG.ford_fulkerson(s,t))

