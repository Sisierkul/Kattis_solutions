import math
import sys

for line in sys.stdin:
    inn = line.split()
    lengd = len(inn)

    coords = []
    for i in range (0, lengd, 2):
        coords.append((float(inn[i]), float(inn[i+1])))
    leftCoord = min(coords)
    rightCoord = max(coords)

    n = len(coords)

    def getSlope(coord1, coord2):
        if coord2[0]-coord1[0] == 0 and coord1[1]>coord2[1]:
            return -10**10
        if coord2[0]-coord1[0] == 0:
            return 10**10
        if coord2[0]-coord1[0]<0 and coord2[1]-coord1[1]<0:
            return -(10**10) 
        return (coord2[1]-coord1[1])/(coord2[0]-coord1[0])

    current_cord = leftCoord
    path = [leftCoord]
    while True:
        maxSlope = -10**10
        newCoord = current_cord
        for coord in coords:
            if coord == leftCoord or coord == current_cord or coord[0]<current_cord[0]:
                continue
            elif getSlope(current_cord, coord) > maxSlope:
                maxSlope = getSlope(current_cord, coord)
                newCoord = coord
        if newCoord == rightCoord:
            path.append(rightCoord)
            current_cord = rightCoord
            break
        path.append(newCoord)
        current_cord = newCoord

    while True:
        maxSlope = -10**10
        newCoord = current_cord
        for coord in coords:
            if coord == rightCoord or coord == current_cord or coord[0]>current_cord[0]:
                continue
            elif getSlope(coord, current_cord) > maxSlope:
                maxSlope = getSlope(coord, current_cord)
                newCoord = coord
        if newCoord == leftCoord:
            break
        path.append(newCoord)
        current_cord = newCoord

    def get_dist(coord1, coord2):
        return math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)

    s = 1
    for i in range (len(path)):
        s+=get_dist(path[i-1], path[i])
    n = len(coords)

    print(100 * n / s)
