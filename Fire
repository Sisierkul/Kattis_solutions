def fire_spread(building, fires, h, w):
    q = []
    counter = 0
    for fire in fires:
        q.append((fire, 0))
        building[fire[0]][fire[1]] = 0
    while counter<len(q):
        corr, time = q[counter]
        counter += 1
        x, y = corr
        #if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            #continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x > h - 1 or new_y < 0 or new_y > w - 1:
                continue
            elif building[new_x][new_y] == '.':
                q.append(((new_x, new_y), time + 1))
                building[new_x][new_y] = time + 1
    return building

def exit_reaching(building, start, h, w):
    q = [(start, 0)]
    visited = [[False for j in range(len(building[0]))] for i in range(len(building))]
    counter = 0
    while counter<len(q):
        corr, time = q[counter]
        counter += 1
        x, y = corr
        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            return time + 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if type(building[new_x][new_y])==int and not visited[new_x][new_y]:
                if building[new_x][new_y] > time+1:
                    q.append(((new_x, new_y), time + 1))
                    visited[new_x][new_y] = True
            elif building[new_x][new_y]!="#" and not visited[new_x][new_y]:
                q.append(((new_x, new_y), time + 1))
                visited[new_x][new_y] = True
    return "IMPOSSIBLE"

def main():
    t = int(input().strip())
    finalString = ''
    for i in range(t):
        w, h = map(int, input().strip().split())
        building = []
        fires = []
        for j in range(h):
            row = list(input().strip())
            if '@' in row:
                start = (j, row.index('@'))
                row = list(map(lambda x: x.replace('@', '.'), row))
            for i in range (w):
                if row[i] == '*':
                    fires.append((j, i))
            building.append(row)
        h = len(building)
        w = len(building[0])
        if fires:
            fire_spread(building, fires, h, w)
        finalString += str(exit_reaching(building, start, h, w)) + '\n'
    print(finalString)
main()
