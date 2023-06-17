c = int(input())

def stigning(c1, c2):
    if (c2[0]-c1[0]) != 0:
        return (c2[1]-c1[1])/(c2[0]-c1[0])
    elif c2[0]-c1[0]>0:
        return 10**10
    else:
        return -10**10

printer = []
for _ in range (c):
    midprint=''
    coords = list(map(float, input().split()))
    coordtups = []
    right= (-10001, 10001,0)
    for i in range (1, len(coords), 2):
        if right[0]<coords[i] or (right[0] == coords[i] and right[1] < coords[i+1]):
            right = (coords[i], coords[i+1], i//2)
        coordtups.append((coords[i], coords[i+1], i//2))
    slopes = []
    sameX = [right]
    for i in coordtups:
        x, y, index = i
        if x == right[0] and y == right[1]:
            continue
        if x == right[0]:
            sameX.append(i)
        else:
            slopes.append((stigning((x,y), (right[0], right[1])), x, y, index))    
    for i in sorted(sameX):
        midprint += str(i[2]) + ' '
    sortedSlopes = sorted(slopes, key=lambda element: (element[0], -element[1]))
    steepest = sortedSlopes[-1][0]
    lastLine = ''
    for i in sortedSlopes:
        if i[0] == steepest:
            lastLine = str(i[3]) + ' ' + lastLine
        else:
            midprint += str(i[3]) + ' '
    printer.append(midprint + lastLine)
for line in printer:
    print(line)
