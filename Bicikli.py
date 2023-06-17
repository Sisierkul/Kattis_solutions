from sys import setrecursionlimit
setrecursionlimit(1000000)

n, m = map(int, input().strip().split())
graph = [[] for _ in range (n+1)]
graph2 = [[] for _ in range (n+1)]
revgraph = [[] for _ in range (n+1)]
tracking = [0] * (n + 1)
tracking[2] = 1

for _ in range (m):
    T1, T2 = map(int, input().strip().split())
    graph[T1].append(T2)
    revgraph[T2].append(T1)

nodes = [False for _ in range (n + 1)]

loop = [False]

def dfs(G, T=2):
    nodes[T] = True
    for town in G[T]:
        if town == 2:
            loop[0] = True
            break
        if not nodes[town]:
            dfs(G,town)
    return nodes

nodes = dfs(revgraph)


for i in range (len(nodes)):
    if nodes[i]:
        graph2[i] = graph[i]

def unique_ways(G, T, vis = [False] * (n + 1)):
    midvis = vis[:]
    midvis[T] = True
    if tracking[T] > 0:
        return tracking[T]
    for town in G[T]:
        if vis[town]:
            loop[0] = True
        elif not loop[0]:
            tracking[T] += unique_ways(G, town, midvis)
    return tracking[T]

if not loop[0]:
    unique_ways(graph2, 1)

if loop[0]:
    print('inf')
else:
    printstr = str(tracking[1])
    if len(printstr)<10:
        print(printstr)
    else:
        print(printstr[-9:])
