from random import randint
from time import sleep
from operator import itemgetter
ordem = []
j = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
print('Valores sortados')
for k, v in j.items():
    sleep(0.3)
    print(f'    O {k}, tirou {v}')
print('Ranking dos Jogadores:')
ordem = sorted(j.items(), key=itemgetter(1), reverse=True)
'''for c, x in j.items():
    if x == min(j.values()) or len(ordem) == 0:
        ordem.append(j[c])
    elif x == max(j.values()):
        ordem.insert(0, j[c])
    else:
        for y in range(0, len(ordem)):
            if x > ordem[y]:
                ordem.insert(y, x)
                break'''
for w, t in enumerate(ordem):
    print(f'{w}º lugar: {t[0]} com {t[1]}')
