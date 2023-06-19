n=int(input())
s=''

for _ in range(n):
    num=(8 * pow(9, int(input())-1, 1000000007)) % 1000000007
    s+=str(num)+'\n'
print(s)
