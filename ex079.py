nl = []
c = 'D'
while True:
    n = (int(input('Digite um Número: ')))
    if n not in nl:
        nl.append(n)
        print('Valor adicionado com sucesso')
    elif n in nl:
        print('Valor duplicado, não vou adicionar')
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sS':
            break
        if c in 'Nn':
            break
    if c in 'Nn':
        break

print('-='*57)
print(f'Voce adicionou os valores: {nl.sort()}')
