from sys import setrecursionlimit
setrecursionlimit(1000000)

n, m, k = map(int, input().strip().split())

grid = []

for x in range (n):
    row = list(input())
    for y in range(m):
        if row[y] == 'S':
            S = (x, y)
        elif row[y] == 'G':
            gold = (x,y)
            row[y] = 1
        elif row[y] == '.':
            row[y] = 1
        elif row[y] == 'F':
            row[y] = 2
        elif row[y] == 'M':
            row[y] = 3
    grid.append(row)

visited = [[(k+3, 10**10) for _ in range(m)] for _ in range(n)]

def find_treasure(grid, start, stamina1 = 0, days1 = 1, prev = None):
    x, y = start
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        stamina = stamina1
        days = days1
        if new_x > n-1 or new_x < 0 or new_y > m - 1 or new_y < 0 or grid[new_x][new_y] == '#' or (new_x, new_y) == S or grid[new_x][new_y]>k or (new_x, new_y) == prev:
            continue
        if k < stamina + grid[new_x][new_y]:
            days += 1
            stamina = 0
        if (visited[new_x][new_y][1]>=days and stamina + grid[new_x][new_y] < visited[new_x][new_y][0]) or visited[new_x][new_y][1]>days:
            visited[new_x][new_y] = (stamina + grid[new_x][new_y], days)
            stamina += grid[new_x][new_y]
            if (new_x, new_y) != gold:
                find_treasure(grid, (new_x, new_y), stamina, days, start)
            

if k == 0:
    print(-1)
else:
    find_treasure(grid, S)
    if not visited[gold[0]][gold[1]][1] == 10**10:
        print(visited[gold[0]][gold[1]][1])
    else:
        print(-1)
