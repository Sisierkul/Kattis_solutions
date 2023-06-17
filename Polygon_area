def Shoelace(coords):
    area = 0
    for i in range(len(coords)):
        if i + 1 == len(coords):
            area += (coords[i][0] * coords[0][1] - coords[0][0] * coords[i][1])
        else:
            area += (coords[i][0] * coords[i+1][1] - coords[i+1][0] * coords[i][1])
    return float(area)/2

myStr = ''

while True:
    n = int(input())
    coords = []
    if n == 0:
        break
    for _ in range(n):
        x, y = map(int, input().strip().split())
        coords.append((x,y))
    A = Shoelace(coords)
    if A < 0:
        myStr += 'CW ' + str(-A) + '\n'
    else:
        myStr += 'CCW ' + str(A) + '\n'

print(myStr)
