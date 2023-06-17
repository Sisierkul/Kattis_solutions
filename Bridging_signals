n = int(input())

numbers = []

for _ in range (n):
    m = int(input())
    numbers.append(m)

def BinSearch(A, l, r, key):
  
    while (r - l > 1):
        m = l + (r - l)//2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def signal_mapping(Connections = numbers, size = n):
   
    chips = [0 for i in range(size + 1)]
    len = 0
   
    chips[0] = Connections[0]
    len = 1
    for i in range(1, size):
        if (Connections[i] < chips[0]):
            chips[0] = Connections[i]
        elif (Connections[i] > chips[len-1]):
            chips[len] = Connections[i]
            len+= 1
        else:
            chips[BinSearch(chips, -1, len-1, Connections[i])] = Connections[i]
    return len

print(signal_mapping())
