import sys

winners = ''

for n in sys.stdin:

    winner = 'Ollie wins.'
    p = 1
    counter = 0

    while p<int(n):
        if counter % 2 == 0:
            p*=9
            winner = 'Stan wins.'
        else:
            p*=2
            winner = 'Ollie wins.'
        counter+=1
    
    winners += winner + '\n'

print(winners)
