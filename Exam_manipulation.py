N=int(input())
myAnswers = input()
hisAnswers = input()
diffAnswers = 0
sameAnswers = 0
for i in range(len(myAnswers)):
    if myAnswers[i] != hisAnswers[i]:
        diffAnswers+=1
    else:
        sameAnswers+=1
if sameAnswers == N:
    print(len(myAnswers))
elif sameAnswers > N:
    print(len(myAnswers) - sameAnswers + N)
else:
    print(len(myAnswers) - N + sameAnswers)
