#fatorial
from time import sleep
n: int = int(input('Digite o número que deseja fatoriar: '))
r = 1
print('Lá vamos nós: {}!'.format(n))
sleep(0.5)
while n > 0:
    r *= n
    print(n, end="")
    print('x' if n > 1 else '=', end='')
    n -= 1
print(r)
'''for x in range(n+1, 1, -1):
    r *= (x - 1)
    if x != 2:
        print(x - 1, end='x')
    elif x == 2:
        print(x - 1, end='=')
print(r)'''
'''x: int == n
while x != 0:
    r = n * (x - 1)'''

