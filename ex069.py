td = h = mn = co = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('Idade: '))
    s = ''
    while s not in 'fFmM':
        s = str(input('Sexo: [M/F] ')).strip()
    co += 1
    if i >= 18:
        td += 1
    if s in 'Mm':
        h += 1
    elif s in 'fF' and i < 20:
        mn += 1
    print('-' * 20)
    c = str(input('Quer continuar? [S/N]'))
    while c not in 'sSnN':
        c = str(input('Quer continuar? [S/N]'))
    if c in 'nN':
        print('FIM DO PROGRAMA')
        break
print(f'Dentre as {co} pessoas cadastradas, {td} tem mais de 18 anos')
print(f'Ao todo temos {h} homens cadastrados;')
print(f'E temos {mn} mulheres com menos de 20 anos')
