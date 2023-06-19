N = int(input())
line = [int(i) for i in input().split()]
line.remove(0)
totalHappiness = 0
for i, x in enumerate(line):
    totalHappiness+= (i+1)*x
s=sum(line)
maxSum = s
midsum = s
for x in range(len(line)):
    midsum-=line[x]
    maxSum = max(maxSum, midsum)
print(totalHappiness + maxSum)
