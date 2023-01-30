from operator import itemgetter
saporra = {}
lg = []
lj = []

while True:
    print('-=' * 35)
    saporra.clear()
    lg.clear()
    saporra['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {saporra["nome"]} jogou: '))
    for x in range(1, p + 1):
        lg.append(int(input(f'Quantos gols na partida {x}: ')))
    saporra['gols'] = lg[:]
    saporra['total'] = sum(lg)
    lj.append(saporra.copy())
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sSNn':
            break
        print('ERRO!! Responda apenas com S ou N.')
    if c in 'Nn':
        break
print('-' * 40)
print('cod nome        gols         total')
print('----------------------------------------')
for k, v in enumerate(lj):
    print(f'{k:>3}', end=' ')
    for j in v.values():
        print(f'{str(j):<12}', end=' ')
    print()
print('----------------------------------------')
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para interromper) '))
    if busca == 999:
        break
    elif busca>= len(lj):
        print(f"ERRO! Não existe jogador com o código {busca}")
    else:
        print('-=' * 35)
        print(f"O jogador {lj[busca]['nome']} jogou {len(lj[busca]['gols'])} partidas.")
        for k, v in enumerate(lj[busca]['gols']):
            print(f'    ==> Na partida {k+1}, fez {v} gols.')
        print(f'Foi um total de {lj[busca]["total"]} gols.')
