n, m = map(int, input().strip().split())

size = 1

while size < n:
    size *= 2

n = size


bit = [0] * (n * 2)

myString = ''

def get_sum(bits, a, b):
    a += n - 1
    b += n - 1
    s = 0
    while a <= b:
        if a % 2 == 1:
            s += bits[a]
            a += 1
        if b % 2 == 0:
            s += bits[b]
            b -= 1
        a //= 2
        b //= 2
    return s

def change(a):
    a += n - 1
    if bit[a] == 1:
        num = -1
    else:
        num = 1
    while a >= 1:
        bit[a] += num
        a //= 2

for _ in range(m):
    inn = input().strip().split()
    if inn[0] == 'F':
        change(int(inn[1]))
    elif inn[0] == 'C':
        myString += str(get_sum(bit, int(inn[1]), int(inn[2]))) + '\n'
    
    

print(myString)
