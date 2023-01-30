lis = ('coca', 'jimo', 'comunismo', 'putaria', 'chocolate', 'coreia', 'perdendo', 'pro', 'brasil')
c: int = 0
for c in lis:
    print(f'\nNa palavra {c} temos as vogais', end=':')
    n = c
    for x in range(0, len(n)):
        if n[x] in 'aeiou':
            print(n[x], end='')
print('Fim Porrra')