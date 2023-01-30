s = 0
lis: list = []
for x in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
    else:
        lis.append(n)
print('A soma dos números pares é {}'.format(s))
print('E está é a lista daqueles não somados \n{}'.format(lis))

