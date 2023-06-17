from collections import defaultdict

n = int(input())

hierarchy = defaultdict(list)
speeds = defaultdict(float)

for _ in range (n):
    child, speed, parent = input().strip().split()
    speeds[child] = float(speed)
    hierarchy[parent].append(child)

dp0 = defaultdict(tuple)
dp1 = defaultdict(tuple)

def dfs(node):
    children = []
    for child in hierarchy[node]:
        children.append(dfs(child))
    sumofchildren0 = 0
    sumofchildren1 = 0
    for kid in children:
        sumofchildren0 += dp1[kid][0]
        sumofchildren1 += dp1[kid][1]
    dp0[node] = (sumofchildren0, sumofchildren1)
    maks = (0,0)
    for x in children:
        j = (1, min(speeds[node], speeds[x]))
        equation = tuple(map(lambda w, x, y, z : w - x + y + z, dp0[node], dp1[x], dp0[x], j))
        if equation > maks:
            maks = equation
    dp1[node] = max(maks, dp0[node])
    return node

dfs(hierarchy['CEO'][0])
pairs = str(dp1[hierarchy['CEO'][0]][0])
speed = str(dp1[hierarchy['CEO'][0]][1] / dp1[hierarchy['CEO'][0]][0])

print(pairs + ' ' + speed)
