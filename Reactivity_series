from collections import defaultdict, deque

n, m = map(int, input().split())
adj_list = defaultdict(list)
indegree = defaultdict(int)

for i in range(m):
    u, v = input().split()
    adj_list[u].append(v)
    indegree[v] += 1

start_node = [u for u in adj_list if indegree[u] == 0]

def topo_sort(graph, indegree):
    order = []
    queue = deque(start_node)
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(graph):
        return False
    return order

if n == 1 and m==0:
    print(0)
elif len(start_node) == 1:
    order = topo_sort(adj_list, indegree)
    valid = True
    if order:
        for x in range(len(order)-1):
            if order[x+1] not in adj_list[order[x]]:
                valid = False
    if not order or len(order) != n or not valid:
        print("back to the lab")
    else:
        print(" ".join(order))
else:
    print("back to the lab")
