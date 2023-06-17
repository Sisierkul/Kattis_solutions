n, m, k = map(int, input().split())

colors = list(map(lambda x: int(x) - 1, input().split()))

C = [[] for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    C[a].append(b)
    C[b].append(a)

DP1 = [[0 for _ in range(5)] for _ in range(n)]
DP2 = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(n)]

for i in range(n):
    for neighbor in C[i]:
        DP1[i][colors[neighbor]] += 1

for i in range(n):
    for neighbor in C[i]:
        for c3 in range(k):
            c4 = colors[neighbor]
            DP2[i][min(c3, c4)][max(c3, c4)] += DP1[neighbor][c3]

ans = 0

for i in range(n):
    for c2 in range(5):
        if c2 == colors[i]:
            continue
        ans += DP1[i][c2]
        for c3 in range(c2 + 1, 5):
            if c3 == colors[i]:
                continue
            ans += DP1[i][c2] * DP1[i][c3] * 2
            for c4 in range(c3 + 1, 5):
                if c4 == colors[i]:
                    continue
                ans += DP1[i][c2] * DP2[i][c3][c4] + DP1[i][c3] * DP2[i][c2][c4] + DP1[i][c4] * DP2[i][c2][c3]
                for c5 in range(c4 + 1, 5):
                    if c5 == colors[i]:
                        continue
                    ans += (DP2[i][c2][c3] * DP2[i][c4][c5] + DP2[i][c2][c4] * DP2[i][c3][c5] + DP2[i][c2][c5] * DP2[i][c3][c4]) * 2

print(ans)
