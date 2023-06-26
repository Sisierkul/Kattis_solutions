N = int(input())
firstList = []
otherList = []

for _ in range (N):
    name, first, other = input().split()
    firstList.append((float(first), float(other), name))
    otherList.append((float(other), float(first), name))

firstRunners = sorted(firstList)[:4]
otherRunners = sorted(otherList)[:4]

speed = 10**10
number1 = 'Sisierkul'

for runner in firstRunners:
    the_runner = runner[2]
    sp = runner[0]
    count = 0
    for runner2 in otherRunners:
        if runner2[2] == the_runner:
            continue
        elif count == 3:
            break
        else: 
            sp += runner2[0]
            count+=1
    if sp < speed:
        speed = sp
        number1 = the_runner
print(speed)
print(number1)
newC = 0
while newC<3:
    if otherRunners[newC][2] == number1:
        otherRunners.pop(newC)
        continue
    print(otherRunners[newC][2])
    newC += 1
