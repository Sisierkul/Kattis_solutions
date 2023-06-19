import math

n = int(input())

def get_dist(coord1, coord2):
    return math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)

def get_center_of_circles(coord1, coord2, d):

    midpoint = [(coord1[0]+coord2[0])/2, (coord1[1]+coord2[1])/2]
    distance_from_midpoint = math.sqrt((d/2)**2 - (get_dist(midpoint, coord2))**2)
    if coord2[0]-coord1[0] == 0:
        slope = 'inf'
    else:
        slope = (coord2[1]-coord1[1])/(coord2[0]-coord1[0])
    if slope == 'inf':
        return ((midpoint[0] + distance_from_midpoint, midpoint[1]),  (midpoint[0] - distance_from_midpoint, midpoint[1]))
    elif slope == 0:
        return ((midpoint[0], midpoint[1] + distance_from_midpoint), (midpoint[0], midpoint[1] - distance_from_midpoint))
    else:
        dir = -1/slope 
        lenOfOneDir = math.sqrt(1 + dir**2)
        vectorsNeeded = distance_from_midpoint / lenOfOneDir
        return ((midpoint[0] + vectorsNeeded, midpoint[1] + dir*vectorsNeeded),(midpoint[0] - vectorsNeeded, midpoint[1] - dir*vectorsNeeded))

printer=[]
for _ in range (n):
    input()
    m, d = input().split()
    m = int(m)
    d = float(d)
    coords = []
    max_mosquitos = 0
    
    for _ in range (m):
        x, y = input().split()
        coords.append((float(x), float(y)))
    else:
        for i in range (m):
            for j in range(i+1, m):
                if get_dist(coords[i],coords[j])>d:
                    continue
                circlepoints = get_center_of_circles(coords[i], coords[j], d)
                for circle in circlepoints:
                    tempMax = 2
                    for k in range(m):
                        if k == i or k == j:
                            continue
                        if get_dist(coords[k], circle)<d/2 + 0.00001:
                            tempMax += 1
                    if tempMax > max_mosquitos:
                        max_mosquitos = tempMax
        printer.append(max_mosquitos)

for num in printer:
    if num == 0:
        num = 1
    print(num)
