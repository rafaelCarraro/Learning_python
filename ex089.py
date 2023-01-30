nota = []
nome = []
tudo = []
j: int = 0
while True:
    nome.append(str(input('Nome do aluno: ')))
    nota.append(float(input('primeira nota: ')))
    nota.append(float(input('Segunda nota: ')))
    nota.append((nota[0]+nota[1])/2)
    nome.append(nota[:])
    tudo.append(nome[:])
    nome.clear()
    nota.clear()
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sS':
            break
        if c in 'Nn':
            break
    if c in 'Nn':
        break
print('=-' * 37)
print('No. NOME      MÉDIA   ')
print('----------------------')
for v, x in enumerate(tudo):
    print(f'{v:<3}{tudo[v][0]:.<10}{tudo[v][1][2]:>4.1f}')
while True:
    print('----------------------')
    j = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if j >= len(tudo) and j != 999:
        j = int(input('Insira um número existente ou 999 para interromper: '))
    elif j == 999:
        print('FINALIZANDO...')
        break
    print(f'Notas de {tudo[j][0]} são {tudo[j][1][:2]}')
print('<<< VOLTE SEMPRE >>>')