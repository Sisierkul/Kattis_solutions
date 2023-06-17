N = int(input())
numbers = []
for _ in range (N):

    A, B = input().split()
    X = max(int(A), int(B))+1
    Y = min(int(A), int(B))+1
    number = Y * 2 - 1
    n=0
    while 2**n<Y:
        n+=1
    new_n = 2**n
    if new_n>X:
        number += X-Y
        numbers.append(number)
        continue
    number+=new_n-Y
    while new_n<X:
        new_n*=2
        number+=Y
    counter = 0
    if X<new_n-Y:
        number-=Y
    else:
        number-=min(Y,new_n-X)
    numbers.append(number)
    
for num in numbers:
    print(num)
