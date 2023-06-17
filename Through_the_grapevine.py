from collections import defaultdict

n, m, d = map(int, input().split())

skeptisism = defaultdict(int)

friends = defaultdict(list)

times_rumored = defaultdict(int)

for _ in range (n):
    name, skept = input().split()
    skeptisism[name] = int(skept)
    times_rumored[name] = 0

for _ in range (m):
    u, v = input().split()
    friends[u].append(v)
    friends[v].append(u)

start = input()

spreaders = [start]

counter = 0
printcount = 0

while spreaders and counter < d:
    new_spreaders = []
    while spreaders:
        spreader = spreaders.pop()
        for person in friends[spreader]:
            if person == start:
                continue
            times_rumored[person]+=1
            if times_rumored[person] == 1:
                printcount+=1
            if times_rumored[person] == skeptisism[person]:
                new_spreaders.append(person)
    counter+=1
    spreaders = new_spreaders

print(printcount)
