class Edge:
	def __init__(self, v, flow, C, rev):
		self.v = v
		self.flow = flow
		self.C = C
		self.rev = rev
#https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/
class Graph:
	def __init__(self, V):
		self.adj = [[] for i in range(V)]
		self.V = V
		self.level = [0 for i in range(V)]

	def addEdge(self, u, v, C):

		a = Edge(v, 0, C, len(self.adj[v]))

		b = Edge(u, 0, 0, len(self.adj[u]))
		self.adj[u].append(a)
		self.adj[v].append(b)

	def BFS(self, s, t):
		for i in range(self.V):
			self.level[i] = -1

		self.level[s] = 0

		q = []
		q.append(s)
		while q:
			u = q.pop(0)
			for i in range(len(self.adj[u])):
				e = self.adj[u][i]
				if self.level[e.v] < 0 and e.flow < e.C:
					self.level[e.v] = self.level[u]+1
					q.append(e.v)
		return False if self.level[t] < 0 else True

	def sendFlow(self, u, flow, t, start):
		if u == t:
			return flow

		while start[u] < len(self.adj[u]):

			e = self.adj[u][start[u]]
			if self.level[e.v] == self.level[u]+1 and e.flow < e.C:

				curr_flow = min(flow, e.C-e.flow)
				temp_flow = self.sendFlow(e.v, curr_flow, t, start)

				if temp_flow and temp_flow > 0:
					e.flow += temp_flow
					self.adj[e.v][e.rev].flow -= temp_flow
					return temp_flow
			start[u] += 1

	def DinicMaxflow(self, s, t):
		if s == t:
			return -1 

		total = 0

		while self.BFS(s, t) == True:

			start = [0 for i in range(self.V+1)]
			while True:
				flow = self.sendFlow(s, float('inf'), t, start)
				if not flow:
					break

				total += flow
		return total

n, m, c = map(int, input().split())

grid = []

d = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(c):
    d[alpha[i]] = i

for _ in range (m):
    grid.append(input())

costs = input().split()

g = Graph((n*m)*1000)



for i in range (m):
    for j in range (n):
        coord = grid[i][j]
        if coord =='B':
            s = i*m+j
        if coord in alpha:
            g.addEdge(i*m+j, n*m + i*m+j, int(costs[d[grid[i][j]]]))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + di, j + dj
            if new_i == -1 or new_i == m or new_j == -1 or new_j == n:
                g.addEdge(i*m+j,0,10**10)
            elif grid[new_i][new_j] in alpha and coord not in alpha:
                g.addEdge(i*m+j, new_i*m+new_j, int(costs[d[grid[new_i][new_j]]]))
            elif grid[new_i][new_j] in alpha and coord in alpha:
                g.addEdge(n*m + i*m+j, new_i*m+new_j, int(costs[d[grid[new_i][new_j]]]))
            elif grid[new_i][new_j] == '.' and coord not in alpha:
                g.addEdge(i*m+j, new_i*m+new_j, 10**10)
            elif grid[new_i][new_j] == '.' and coord in alpha:
                g.addEdge(n*m + i*m+j, new_i*m+new_j, 10**10)
price = g.DinicMaxflow(s, 0)
if price > 10**10-1:
	print(-1)
else:
	print(price)
