n = int(input())

coords = []

for _ in range(n):
    x, y = map(float, input().strip().split())
    coords.append((x,y))

coords.sort()

L = 0

for i in range(n-1):
    L_candidate = (abs(coords[i][1] - coords[i+1][1]))/abs(coords[i][0] - coords[i+1][0])
    if L_candidate > L:
        L = L_candidate

print(L)
