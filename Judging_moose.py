l, r = input().split()
age = 2 * max(int(l), int(r))
if l == r == '0':
    print('Not a moose')
elif l == r:
    print('Even', str(age))
else:
    print('Odd', str(age))
