from collections import defaultdict

n = int(input())
primes = [0 for _ in range (1000000)]

def factorize(n):
    L=[]
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                L.append(i)
                break
    return(L)

primes = [0 for _ in range (1000000)]
numbers = [int(i) for i in input().split()]
totalScore = 1
checker = []
factorss = []

def listChecker(list1, list2):
    ans = 0
    for v in list1:
        if v in list2:
            list2.remove(v)
        else:
            ans+=1
    return ans

finalAns = 0
checkList = []

for num in numbers:
    prime = factorize(num)
    factorss.append(prime)
    for i in prime:
        primes[i] += 1
        if primes[i]%n==0:
            checkList.append(i)
            totalScore*=i
            checker.append(i)

for P in factorss:
    finalAns += listChecker(checkList, P)

print(str(totalScore) + ' ' + str(finalAns))
