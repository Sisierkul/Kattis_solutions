n=int(input())

myString = ''

for _ in range (n):
    a, b, c, d = map(int, input().strip().split())  
    if d == 2:
        myString += str((max(((a+d)**2+b**2+c**2 + 7*min(a+d, b, c)),((b+d)**2+a**2+c**2) + 7*min(b+d, a, c), ((c+d)**2+b**2+a**2) + 7*min(c+d, b, a), ((a+1)**2+(b+1)**2+c**2 + 7*min(a+1, b+1, c)),((c+1)**2+(b+1)**2+a**2 + 7*min(a, b+1, c+1)), ((a+1)**2+(c+1)**2+b**2 + 7*min(a+1, b, c+1))))) + '\n'
    elif d == 3:
        myString += str((max(((a+d)**2+b**2+c**2 + 7*min(a+d, b, c)),((b+d)**2+a**2+c**2) + 7*min(b+d, a, c), ((c+d)**2+b**2+a**2) + 7*min(c+d, b, a), ((a+2)**2+(b+1)**2+c**2 + 7*min(a+2, b+1, c)),((c+1)**2+(b+2)**2+a**2 + 7*min(a, b+2, c+1)), ((a+2)**2+(c+1)**2+b**2 + 7*min(a+2, b, c+1)),((a+1)**2+(c+2)**2+b**2 + 7*min(a+1, b, c+2)), ((b+2)**2+(a+1)**2+c**2 + 7*min(a+1, b+2, c)),((c+2)**2+(b+1)**2+a**2 + 7*min(a, b+1, c+2)), ((a+1)**2+(c+1)**2+(b+1)**2 + 7*min(a+1, b+1, c+1))))) + '\n'
    else:
        myString += str((max(((a+d)**2+b**2+c**2 + 7*min(a+d, b, c)),((b+d)**2+a**2+c**2) + 7*min(b+d, a, c), ((c+d)**2+b**2+a**2) + 7*min(c+d, b, a)))) + '\n'

print(myString)
