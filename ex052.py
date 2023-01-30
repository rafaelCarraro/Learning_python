n = int(input('Digite um número: '))
u = 0
for c in range(1, n+1):
    r = n % c
    if r != 0:
        continue
    u += 1
if u == 2:
    print('O número {} foi dividido {} vezes, portanto é primo'.format(n, u))
else:
    print('O número {}, foi dividido {} vezes, portanto não é primo'.format(n, u))
