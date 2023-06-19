n = int(input())

matrix = []

for _ in range (n):
    row = input().split()
    row = [int(i) for i in row]
    matrix.append(row)

impossible = False

newMatrix = []

for i in range (n):
    row = []
    if impossible:
        break
    for j in range(n):
        if i == j:
            row.append(matrix[i][j])
            continue
        if (max(matrix[i][j], matrix[j][i]) - min(matrix[i][j], matrix[j][i]))%2 == 1:
            impossible = True
            break
        if matrix[i][j] == matrix[j][i]:
            row.append(matrix[i][j])
        elif matrix[i][j] > matrix[j][i]:
            row.append((max(matrix[i][j], matrix[j][i]) - min(matrix[i][j], matrix[j][i]))//2)
        else:
            row.append(-(max(matrix[i][j], matrix[j][i]) - min(matrix[i][j], matrix[j][i]))//2)
    newMatrix.append(row)

if impossible:
    print(-1)
elif matrix == newMatrix:
    print(1)
    for row in matrix:
        print(' '.join(map(str, row)))
else:
    matrix2 = [[0 for _ in range (n)] for _ in range (n)]
    for i in range(n):
        for j in range(n):
            matrix2[i][j] = matrix[i][j] - newMatrix[i][j]
    print(2)
    for row in newMatrix:
        print(' '.join(map(str, row)))
    for row in matrix2:
        print(' '.join(map(str, row)))
