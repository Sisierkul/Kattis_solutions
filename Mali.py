def solve(A, B):
    C=A[:]
    D=B[:]
    myMax = 0
    Ccounter = 0
    Dcounter = 99
    while Ccounter < 100 and Dcounter >= 0:
        if C[Ccounter] > 0 and D[Dcounter] > 0 and Ccounter + Dcounter + 2 > myMax:
            myMax = Ccounter + Dcounter + 2
        if C[Ccounter] < D[Dcounter]:
            D[Dcounter] -= C[Ccounter]
            Ccounter += 1
        elif C[Ccounter] > D[Dcounter]:
            C[Ccounter] -= D[Dcounter]
            Dcounter -= 1
        else:
            Ccounter += 1
            Dcounter -= 1
    return myMax

n = int(input().strip())
A = [0]*100
B = [0]*100
numbers = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    A[a-1] += 1
    B[b-1] += 1 
    numbers.append(solve(A,B))

for num in numbers:
    print(num)
