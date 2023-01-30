from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram:', end=' ')
v = sorted(n)
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior néumero é {v[len(v)-1]}, já o menor é {v[0]}')
print(f'O maior valor foi {max(n)}, já o menor é {min(n)}')
