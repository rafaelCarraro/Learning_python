from random import randint
from time import sleep
jogo: list = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30,)
r = int(input('Quantos jogos você deseja sortear? '))
print(f'-=-=-=  SORTEANDO {r:^3} JOGOS -=-=-=')
for x in range(0, r):
    sleep(0.3)
    while len(jogo) < 6:
        n = randint(0, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    print(f'Jogo {x+1}: {jogo}')
    jogo.clear()
print(f'=-=-=-=-=< BOA SORTE! >-=-=-=-=-')
