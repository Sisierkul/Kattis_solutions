
 Download file
from collections import defaultdict

n, m = map(int, input().strip().split())

positions = [[500, 500] for _ in range (n+1)]

isKnown = [False for _ in range (n+1)]

bonds = defaultdict(list)

for i in range (1, n + 1):
    x, y = map(int, input().strip().split())
    if x != -1 and y != -1:  
        positions[i] = [x, y]
        isKnown[i] = True

for _ in range (m):
    a, b = map(int, input().strip().split())
    bonds[a].append(b)
    bonds[b].append(a)

def find_avg_pos(neighbors):
    xsum = 0
    ysum = 0
    for j in neighbors:
        xsum += positions[j][0]
        ysum += positions[j][1]
    xpos = float(xsum) / len(neighbors)
    ypos = float(ysum) / len(neighbors)
    return [xpos, ypos]

for _ in range (16000):
    for i in range (1,n+1):
        if not isKnown[i]:
            positions[i] = find_avg_pos(bonds[i])

myStr = ''

for i in range(1, n+1):
    x, y = positions[i]
    myStr += str(x) + ' ' + str(y) + '\n'

print(myStr)
