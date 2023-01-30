gp = 0
pp = 2000
for x in range(1, 6):
    p = float(input('Digite o peso da {} pessoa: '.format(x)))
    if gp < p:
        gp = p
    elif pp > p:
        pp = p
print('O maior peso foi {}, já o menor {}'.format(gp, pp))
