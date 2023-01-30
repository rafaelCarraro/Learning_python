pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    pessoa.clear()
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sSNn':
            break
        print('ERRO!! Responda apenas com S ou N.')
    if c in 'Nn':
        break
media = soma / len(galera)
print('-=' * 30)
print(f'-Ao todo temos {len(galera)} pessoas cadastradas:')
print(f'-A a média de idade é {media:.1f} anos')
print('-As mulheres cadastradas foram, ', end= '')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=" ")
print('\nLista das pessoas com a idade acima da média:')
for p in galera:
    if p['idade'] > media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<<< ENCERRADO >>>')
