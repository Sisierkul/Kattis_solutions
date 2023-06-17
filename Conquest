from sys import setrecursionlimit
setrecursionlimit(1000000)
from collections import defaultdict
import heapq

n, m = map(int, input().strip().split())

kingdom = [[] for _ in range (n+1)]

army_sizes = [0 for _ in range(n+1)]

for _ in range (m):
    u, v = map(int, input().strip().split())
    kingdom[u].append(v)
    kingdom[v].append(u)

for i in range (n):
    s = int(input())
    army_sizes[i+1] = s

myStr = ''

heap = []

for neighbor in kingdom[1]:
    heapq.heappush(heap, (army_sizes[neighbor], neighbor))

while heap:
    army, island = heapq.heappop(heap)
    if army_sizes[island] == 10**10 or island == 1:
        continue
    if army < army_sizes[1]:
        army_sizes[1] += army
        army_sizes[island] = 10**10
        for neighbor in kingdom[island]:
            heapq.heappush(heap, (army_sizes[neighbor], neighbor))
    else:
        break



print(army_sizes[1])
