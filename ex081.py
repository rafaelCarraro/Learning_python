nl = []
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
nl.sort(reverse = True)
print('-=' * 35)
print(f'Você digitou {len(nl)} elementos;')
print(f'Os valores em ordem decrescente são: {nl};')
print('O valor 5 faz parte da Lista!'if 5 in nl else 'O valor 5 não faz parte da Lista!')
