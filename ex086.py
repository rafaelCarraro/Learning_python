matriz = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for c, v in enumerate(matriz):
    for x in range(0, 3):
        matriz[c][x] = int(input(f'Digite um valor para [{c}, {x}]:'))
print('-=' * 25)
for l in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[l][p]:^4}]', end='')
    print()
'''for p, pp in enumerate(matriz[0]):
    print(f'[{matriz[0][p]:^3}]', end='')
print('\n', end='')
for s, ss in enumerate(matriz[1]):
    print(f'[{matriz[1][s]:^3}]',end='')
print('\n', end='')
for t, tt in enumerate(matriz[2]):
    print(f'[{matriz[2][t]:^3}]', end='')'''
