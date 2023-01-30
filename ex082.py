nl = []
pl = []
il = []
while True:
    n = (int(input('Digite um Número: ')))
    nl.append(n)
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sS':
            break
        if c in 'Nn':
            break
    if c in 'Nn':
        break
for x in range(0, len(nl)):
    if nl[x] % 2 == 0:
        pl.append(nl[x])
    elif nl[x] % 2 == 1:
        il.append(nl[x])
print(f'A lista completa é {nl}')
print(f'A lista com os números pares é {pl}')
print(f'A lista com os números ímpares é {il}')

