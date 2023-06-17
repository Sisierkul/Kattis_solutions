def count_subsequences(d, n, a):
    count = [0] * d
    cum_sum = 0
    res = 0
    for i in range(n):
        cum_sum = (cum_sum + a[i]) % d
        res += count[cum_sum]
        count[cum_sum] += 1
    res += count[0]
    return res

c = int(input().strip())
numbers = []
for _ in range(c):
    d, n = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    numbers.append(count_subsequences(d, n, a))
for num in numbers:
    print(num)
