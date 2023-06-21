N = int(input())
K = int(input())

store_items = [[] for _ in range (N)]

for _ in range (K):
    store, item = input().split()
    store_items[int(store)].append(item)

M = int(input())

bought = []

for _ in range (M):
    bought.append(input())

output = 'impossible'

rev_bought = []
i = 0
path = []
while bought:
    if i == N:
        break
    item = bought.pop()
    rev_bought.append(item)
    while i<N:
        if item in store_items[N - i - 1]:
            path.append(N - i - 1)
            break
        i+=1
    if not bought:
        output = 'ambiguous'
if output == 'ambiguous':
    j = 0
    rev_path = []
    while rev_bought:
        if j == N:
            break
        item = rev_bought.pop()
        while j<N:
            if item in store_items[j]:
                rev_path.append(j)
                break
            j+=1
    if rev_path[::-1] == path:
        output = 'unique'
print(output)
