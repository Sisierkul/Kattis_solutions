from collections import defaultdict

n=int(input())
words = defaultdict(int)

printList = []

for _ in range (n):
    word = input()
    if word in words:
        printList.append(words[word])
        for i in range(-(len(word)-1), 0):
            words[word[:i]]+=1
        words[word] += 1
    else:
        printList.append(0)
        for i in range(-(len(word)-1), 0):
            words[word[:i]]+=1
        words[word]+=1
for w in printList:
    print(w)
